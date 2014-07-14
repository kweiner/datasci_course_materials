import sys
import json
import re

def load_scores(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores
    
def compute_score(tweet_words, scores):
    total_score = 0
    for word in tweet_words:
        if (word in scores):
            score = scores[word]
            total_score += score
    return total_score

def get_words(text):
    parts = re.compile("\s").split(text)
    words = [re.sub(ur'[\W_]+', u'', part, flags=re.UNICODE).lower().strip() for part in parts]
    words = [i for i in words if len(i) > 0 and (i[0].isdigit() or i[0].isalpha())]
    return words

def get_states():
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    return states

def calc(location_parts, happy_states, happy_states_count, sent_score, states):
    for location_part in location_parts:
        for state in states:
            if location_part == states[state].lower() or location_part == state.lower():
                happy_states[state] = happy_states.get(state, 0) + sent_score
                happy_states_count[state] = happy_states_count.get(state, 0) + 1
                return state

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = load_scores(sent_file)
    states = get_states()
    
    happy_states = {}
    happy_states_count = {}

    with tweet_file:
        for line in tweet_file:
            message = json.loads(line)
            if 'text' in message:
                if 'user' in message:
                    user = message['user']
                    if 'location' in user:
                        tweet_text = message['text']
                        tweet_words = get_words(tweet_text)
                        sent_score = compute_score(tweet_words, scores)

                        location = user['location']
                        location_parts = get_words(location)
                        state = calc(location_parts, happy_states, happy_states_count, sent_score, states)
                        #if state == 'CA':
                        #    print state,sent_score,happy_states[state],happy_states_count[state]
    
    state_avgs = {}
    for state in states:
         if state in happy_states:
             avg = happy_states[state] / float(happy_states_count[state])
             state_avgs[state] = avg
    
    print sorted(state_avgs.items(), key=lambda x:x[1], reverse=True)[0][0]

if __name__ == '__main__':
    main()
