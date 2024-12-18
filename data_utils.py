from data_info import annotator_demographic_axes, options_to_text, comment_annotations
# from data_info import meta_data, comment_annotations, target_demographic_axes, annotator_demographic_additional
from prompts import demographic_specific_prompt, option_type, identities_prompt, identities_subprompt, extra_prompts
import numpy as np
import pandas as pd
from collections import defaultdict
from tqdm import tqdm
from collections import Counter

# ----------------------------------------- OPENAI UTILS -----------------------------------------
def openai_messages_format(system, user):
    '''
    Formats prompts in client.chat.completions.create messages format
    '''
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]
    return messages

def openai_messages_add_response(messages, assistant, user):
    '''
    adds response from assistant and additional user prompt to messages in client.chat.completions.create format
    '''
    messages.append({"role": "assistant", "content": assistant})
    messages.append({"role": "user", "content": user})
    return messages

def openai_get_generation(client, model, messages):
    '''
    Prompts a given openai model with messages
    '''
    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )
    response = completion.choices[0].message.content
    return response

def openai_iter_generation(client, model, system, user_list):
    '''
    Iteratively prompts a model with a list of prompts (user_list) to ask in order
    '''
    responses = []
    messages = openai_messages_format(system, user_list[0])
    assistant = openai_get_generation(client, model, messages)
    responses.append(assistant)
    for user in user_list[1:]:
        messages = openai_messages_add_response(messages, assistant, user)
        assistant = openai_get_generation(client, model, messages)
        responses.append(assistant)
    return responses

# ----------------------------------------- PROMPTING UTILS -----------------------------------------

def get_true_annotator_demographics(instance, axis):
    '''
    For annotator demographics where many answers are possible, returns a list given the data instance and axis interested in.
    '''
    to_ret = []
    for option in annotator_demographic_axes[axis]:
        data_key = "annotator_" + axis + "_" + option
        if instance[data_key] == True:
            to_ret.append(option)
    if len(to_ret) == 0:
        return ["other"]
    return to_ret

def get_annotator_demographic_dict(data_instance):
    '''
    Returns a dictionary of demographics for the annotator. Race, sexuality, and religion can have multiple answers selected.
    '''
    demographic_dict = {}
    demographic_dict['gender'] = data_instance['annotator_gender']
    demographic_dict['race'] = get_true_annotator_demographics(data_instance, 'race')
    demographic_dict['income'] = data_instance['annotator_income']
    demographic_dict['educ'] = data_instance['annotator_educ']
    demographic_dict['ideology'] = data_instance['annotator_ideology']
    demographic_dict['age'] = data_instance['annotator_age']
    demographic_dict['sexuality'] = get_true_annotator_demographics(data_instance, 'sexuality')
    demographic_dict['trans'] = data_instance['annotator_trans']
    demographic_dict['religion'] = get_true_annotator_demographics(data_instance, 'religion')
    return demographic_dict

def get_demographic_system_prompt(data_instance, axes_to_include):
    '''
    Returns a system prompt given a data instance and axes to include, 
    such that the system instructions matches the demographic info of the data instance.
    '''
    instructions = demographic_specific_prompt['prompt']
    annotator_demographic_dict = get_annotator_demographic_dict(data_instance)
    for axis in axes_to_include:
        if type(annotator_demographic_dict[axis]) == str:
            to_replace = options_to_text[annotator_demographic_dict[axis]]
        elif type(annotator_demographic_dict[axis]) == float: # for age
            to_replace = str(annotator_demographic_dict[axis])
        else:
            to_replace_lst = []
            for option in annotator_demographic_dict[axis]:
                to_replace_lst.append(options_to_text[option])
            to_replace = ", ".join(to_replace_lst)
        replaced = "[" + axis + "]"
        instructions += " " + demographic_specific_prompt[axis].replace(replaced, to_replace)
    return instructions

def get_identities_survey_prompt(comment):
    '''
    Returns the initial survey prompt, given the comment being evaluated
    '''
    prompt = identities_prompt['prompt'].replace("[COMMENT]", comment)
    prompt += "\n" + ", ".join(identities_prompt['options'])
    prompt += "\n" + option_type[identities_prompt['select_type']]
    return prompt

def get_identities_subprompts(options):
    '''
    Returns the second survey prompt, given the options the LLM identified as targeted groups
    '''
    subprompts = []
    for option in options:
        prompt = identities_subprompt['prompt'].replace("[OPTION]", option)
        prompt += "\n" + ", ".join(identities_prompt[option])
        prompt += "\n" + option_type[identities_subprompt['select_type']]
        subprompts.append(prompt)
    return subprompts

def get_extra_survey_prompts(prompt_options):
    '''
    Returns the follow up prompts for rating along various axes
    '''
    prompts = []
    # options are: ['sentiment', 'respect', 'insult', 'humiliate', 'status', 'dehumanize', 'violence', 'genocide', 'attack_defend', 'hatespeech']
    for p in prompt_options:
        prompt = extra_prompts[p]['prompt']
        prompt += "\n" + ", ".join(extra_prompts[p]['options'])
        prompt += "\n" + option_type[extra_prompts[p]['select_type']]
        prompts.append(prompt)
    return prompts


# ----------------------------------------- MAJORITY VOTING -----------------------------------------

def get_majority_vote(data):
    '''
    data = {
        'comment': '...',
        'sentiment': [score, score...], 
        'respect': [score, score...], 
        'insult': [score, score...], 
        'humiliate': [score, score...], 
        'status': [score, score...], 
        'dehumanize': [score, score...], 
        'violence': [score, score...], 
        'genocide': [score, score...], 
        'attack_defend': [score, score...], 
        'hatespeech': [score, score...]
    }
    '''
    majority_vote = {}
    for axis in comment_annotations:
        c = Counter(data[axis])
        value, count = c.most_common()[0]
        majority_vote[axis] = value
    return majority_vote

# ----------------------------------------- DAWID-SKENE -----------------------------------------

def get_ds_format(data, axis):
    '''
    Formats data like {comment_id_1: {annotator_id_1: [score], annotator_id_2: [score],...}, comment_id_2: {...}}
    '''
    to_ret = {}
    for instance in data:
        if instance['comment_id'] not in to_ret.keys():
            to_ret[instance['comment_id']] = {}
        to_ret[instance['comment_id']][instance['annotator_id']] = [instance[axis]]
    return to_ret