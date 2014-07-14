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

def compute_tweet_words(tweet_text):
    parts = re.compile("\s").split(tweet_text)
    words = [re.sub(ur'[\W_]+', u'', part, flags=re.UNICODE).lower().strip() for part in parts]
    words = [i for i in words if len(i) > 0 and (i[0].isdigit() or i[0].isalpha())]
    return words

def main():
    tweet_file = open(sys.argv[1])
    
    term_counts = {}

    with tweet_file:
        for line in tweet_file:
            message = json.loads(line)
            if 'text' in message:
                tweet_text = message['text']
                tweet_words = compute_tweet_words(tweet_text)
                for word in tweet_words:
                    if word in term_counts:
                        term_counts[word] = term_counts[word] + 1
                    else:
                        term_counts[word] = 1
                        
    total_count = sum(term_counts.values())
    
    sorted_term_counts = sorted(term_counts)
    for k in sorted_term_counts:
        try:
            tf = term_counts[k] / float(total_count)
            print k,tf
        except UnicodeEncodeError:
            pass
    #print total_count

if __name__ == '__main__':
    main()
