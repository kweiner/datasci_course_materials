import sys
import json
import re

def load_scores(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def compute_score(tweet_text, scores):
    total_score = 0
    for term, score in scores.iteritems():
        a = re.compile(".*\\b" + term + "\\b.*")
        match = a.match(tweet_text)
        if match:
            total_score += score
    return total_score
    
def compute_score_fast(tweet_words, scores):
    total_score = 0
    for word in tweet_words:
        if (word in scores):
            score = scores[word]
            total_score += score
    return total_score

def compute_tweet_words(tweet_text):
    parts = re.compile("\s").split(tweet_text)
    words = [re.sub(ur'[\W_]+', u'', part, flags=re.UNICODE) for part in parts]
    return words

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = load_scores(sent_file)

    with tweet_file:
        for line in tweet_file:
            message = json.loads(line)
            if 'text' in message:
                tweet_text = message['text']
                tweet_words = compute_tweet_words(tweet_text)
                sent_score = compute_score_fast(tweet_words, scores)
                #print sent_score
                #print tweet_text
                unique_words = set(tweet_words)
                for word in unique_words:
                    if not word in scores:
                        print word,sent_score
                #print "-------"

if __name__ == '__main__':
    main()
