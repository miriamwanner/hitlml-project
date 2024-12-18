

demographic_specific_prompt = {
    'prompt': "You are a person with the following demographic attributes. You identify with all of these attributes.",
    'gender': "Your gender is [gender].", # from the additional info
    'race': "Your race is [race].", # from the true/false axes
    'income': "You make [income]$ a year.", # from the additional info
    'educ': "Your highest level of education is [educ].", # from the additional info
    'ideology': "You identify as [ideology] on the political spectrum.", # from the additional info
    'age': "You are [age] years old.", # from the additional info
    'sexuality': "Your sexuality is [sexuality].", # from the true/false axes
    'trans': "You [trans] transgender.", # from the additional info 'trans'
    'religion': "You practice [religion]." # from the true/false axes
}

option_type = {
    "multi-select": "You can select multiple choices. Respond with a comma separated list of your selections and nothing else.",
    "single-select": "You can only select one option. Respond with your answer choice and nothing else."
}

identities_prompt = {
    'prompt': "Comment: [COMMENT]\nIs the comment above directed at or about any individual or groups based on:",
    'options': ["race or ethnicity", "religion", "national origin or citizenship status", "gender", "sexual orientation", "age", "disability status", "none of the above"],
    'select_type': "multi-select"
}

identities_subprompt = {
    'prompt': "You identified [OPTION] as a targeted group by this prompt. Which of the following specific groups is this comment directed towards:",
    'race or ethnicity': ['asian', 'black', 'latinx', 'middle_eastern', 'native_american', 'pacific_islander', 'white', 'other'],
    'religion': ['athiest', 'buddhist', 'christian', 'hindu', 'jewish', 'mormon', 'muslim', 'other'],
    'national origin or citizenship status': ['immigrant', 'migrant_worker', 'specific_country', 'undocumented', 'other'],
    'gender': ['men', 'non_binary', 'transgender_men', 'transgender_unspecified', 'transgender_women', 'women', 'other'],
    'sexual orientation': ['bisexual', 'gay', 'lesbian', 'straight', 'other'],
    'age': ['children', 'teenagers', 'young_adults', 'middle_aged', 'seniors', 'other'],
    'disability status': ['physical', 'cognitive', 'neurological', 'visually_impaired', 'hearing_impaired', 'unspecific', 'other'],
    'select_type': 'multi-select'
}

extra_prompts = {
    "sentiment": {
        'prompt': "How would you describe the sentiment of this comment?",
        'options': ["strongly negative", "somewhat negative", "neutral", "somewhat positive", "strongly positive"], # on a scale of 0-4
        'select_type': "single-select"
    },

    "respect": {
        'prompt': "Is this comment respectful towards the group(s) you previously identified?",
        'options': ["strongly disrespectful", "disrespectful", "neutral", "respectful", "strongly respectful"], # on a scale of 0-4
        'select_type': "single-select"
    },

    "insult": {
        'prompt': "Do you agree or disagree with the following statement: This comment is insulting towards the group(s) you previously identified.",
        'options': ["strongly disagree", "disagree", "neither disagree nor agree", "agree", "strongly agree"], # on a scale of 0-4
        'select_type': "single-select"
    },

    "humiliate": {
        'prompt': "Do you agree or disagree with the following statement: This comment is humiliating towards the group(s) you previously identified.",
        'options': ["strongly disagree", "disagree", "neither disagree nor agree", "agree", "strongly agree"], # on a scale of 0-4
        'select_type': "single-select"
    },

    "status": {
        'prompt': "This comment states that the group(s) you previously identified is:",
        'options': ["strongly inferior", "inferior", "neither superior nor inferior", "superior", "strongly superior"], # on a scale of 0-4
        'select_type': "single-select"
    },

    "dehumanize": {
        'prompt': "Do you agree or disagree with the following statement: This comment dehumanizes the group(s) you previously identified (e.g., by comparing them to an animal).",
        'options': ["strongly disagree", "disagree", "neither disagree nor agree", "agree", "strongly agree"], # on a scale of 0-4
        'select_type': "single-select"
    },

    "violence": {
        'prompt': "Do you agree or disagree with the following statement: This comment calls for using violence against the group(s) you previously identified.",
        'options': ["strongly disagree", "disagree", "neither disagree nor agree", "agree", "strongly agree"], # on a scale of 0-4
        'select_type': "single-select"
    },

    "genocide": {
        'prompt': "Do you agree or disagree with the following statement: This comment calls for the deliberate killing of a large group of people from the group(s) you previously identified.",
        'options': ["strongly disagree", "disagree", "neither disagree nor agree", "agree", "strongly agree"], # on a scale of 0-4
        'select_type': "single-select"
    },

    "attack_defend": {
        'prompt': "Is the comment attacking or defending the group(s) you previously identified?",
        'options': ["strongly defending", "defending", "neither defending nor attacking", "attacking", "strongly attacking"], # on a scale of 0-4
        'select_type': "single-select"
    },

    "hatespeech": {
        'prompt': "Does this comment contain hate speech, defined as \"bias-motivated, hostile and malicious language targeted at a person/group because of their actual or perceived innate characteristics, especially when the group is unnecessarily labeled (e.g., \"jew bankers\", \"nâĂŞ hooligans\").\" The comment contains hate speech if slurs or derogatory language are used toward any person or group regardless of whether or not the target is a member of the slur-target group. (e.g. a comment calling Trump a faggot or a n***** still contains hate speech).",
        'options': ["yes", "no", "unclear"],
        'select_type': "single-select"
    }
}    

