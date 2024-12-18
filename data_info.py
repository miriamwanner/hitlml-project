

meta_data = ['comment_id', 'annotator_id', 'platform', 'text', 'annotator_severity', 'hate_speech_score'] # I believe the hate speech score is given by the paper

comment_annotations = ['sentiment', 'respect', 'insult', 'humiliate', 'status', 'dehumanize', 'violence', 'genocide', 'attack_defend', 'hatespeech']

both_demographic_axes = {
    'race': ['asian', 'black', 'latinx', 'middle_eastern', 'native_american', 'pacific_islander', 'white', 'other'],
    'religion': ['atheist', 'buddhist', 'christian', 'hindu', 'jewish', 'mormon', 'muslim', 'other'],
    'gender': ['men', 'non_binary', 'women'],
    'sexuality': ['bisexual', 'gay', 'straight', 'other'],
}

target_demographic_axes = {
    'race': ['asian', 'black', 'latinx', 'middle_eastern', 'native_american', 'pacific_islander', 'white', 'other'],
    'religion': ['atheist', 'buddhist', 'christian', 'hindu', 'jewish', 'mormon', 'muslim', 'other'],
    'origin': ['immigrant', 'migrant_worker', 'specific_country', 'undocumented', 'other'],
    'gender': ['men', 'non_binary', 'transgender_men', 'transgender_unspecified', 'transgender_women', 'women', 'other'],
    'sexuality': ['bisexual', 'gay', 'lesbian', 'straight', 'other'],
    'age': ['children', 'teenagers', 'young_adults', 'middle_aged', 'seniors', 'other'],
    'disability': ['physical', 'cognitive', 'neurological', 'visually_impaired', 'hearing_impaired', 'unspecific', 'other']
}

annotator_demographic_axes = {
    'gender': ['men', 'women', 'non_binary', 'prefer_not_to_say', 'self_describe'],
    'education': ['some_high_school', 'high_school_grad', 'some_college', 'college_grad_aa', 'college_grad_ba', 'professional_degree', 'masters', 'phd'],
    'income': ['<10k', '10k-50k', '50k-100k', '100k-200k', '>200k'],
    'ideology': ['extremeley_conservative', 'conservative', 'slightly_conservative', 'neutral', 'slightly_liberal', 'liberal', 'extremeley_liberal', 'no_opinion'],
    'race': ['asian', 'black', 'latinx', 'middle_eastern', 'native_american', 'pacific_islander', 'white', 'other'],
    'sexuality': ['bisexual', 'gay', 'straight', 'other'],
    'religion': ['atheist', 'buddhist', 'christian', 'hindu', 'jewish', 'mormon', 'muslim', 'other']
}

annotator_demographic_additional = { # options in the list
    'gender': ['male', 'female'],
    'trans': ['no', 'yes'], # and something else I can't tell
    'educ': ['some_high_school', 'high_school_grad', 'some_college', 'college_grad_aa', 'college_grad_ba', 'professional_degree', 'masters', 'phd'],
    'income': ['<10k', '10k-50k', '50k-100k', '100k-200k', '>200k'],
    'ideology': ['extremeley_conservative', 'conservative', 'slightly_conservative', 'neutral', 'slightly_liberal', 'liberal', 'extremeley_liberal', 'no_opinion'],
    'transgender': [True, False],
    'cisgender': [True, False],
    'transgender_prefer_not_to_say': [True, False],
    'age': ['children_0-12', 'teenagers_13-17', 'young_adults_18-39', 'middle_aged_40-64', 'seniors_65-150', 'other'] # age is given as a number
}

not_used = ['infitms', 'outfitms', 'std_err', 'annotator_infitms', 'annotator_outfitms', 'hypothesis']

options_to_text = {
    'male': 'male', 'female': 'female',
    'asian': 'asian', 'black': 'black', 'latinx': 'latinx', 'middle_eastern': 'middle eastern', 'native_american': 'native american', 'pacific_islander': 'pacific islander', 'white': 'white', 'other': 'unknown',
    '<10k': 'less than 10k', '10k-50k': 'between 10k and 50k', '50k-100k': 'between 50k and 100k', '100k-200k': 'between 100k and 200k', '>200k': 'more than 200k',
    'some_high_school': 'some high school', 'high_school_grad': 'high school graduate', 'some_college': 'some college', 'college_grad_aa': 'college graduate with an AA', 'college_grad_ba': 'college graduate with a BA', 'professional_degree': 'a professional degree', 'masters': 'a masters degree', 'phd': 'a PhD',
    'extremeley_conservative': 'extremely conservative', 'conservative': 'conservative', 'slightly_conservative': 'slightly conservative', 'neutral': 'neutral', 'slightly_liberal': 'slightly liberal', 'liberal': 'liberal', 'extremely_liberal': 'extremely liberal', 'no_opinion': 'unknown',
    'bisexual': 'bisexual', 'gay': 'gay', 'straight': 'straight', 'other': 'unknown',
    'no': 'are not', 'yes': 'are',
    'atheist': 'atheism', 'buddhist': 'Buddhism', 'christian': 'Christianity', 'hindu': 'Hinduism', 'jewish': 'Judaism', 'mormon': 'Mormonism', 'muslim': 'the Muslim religion', 'other': 'an unknown religion'
}

response_to_num = {
        "strongly negative": 0, "somewhat negative": 1, "neutral": 2, "somewhat positive": 3, "strongly positive": 4,
        "strongly disrespectful": 0, "disrespectful": 1, "neutral": 2, "respectful": 3, "strongly respectful": 4,
        "strongly disagree": 0, "disagree": 1, "neither disagree nor agree": 2, "agree": 3, "strongly agree": 4,
        "strongly inferior": 0, "inferior": 1, "neither superior nor inferior": 2, "superior": 3, "strongly superior": 4,
        "strongly defending": 0, "defending": 1, "neither defending nor attacking": 2, "attacking": 3, "strongly attacking": 4,
        "yes": 1, "no": 0, "unclear": 2
}