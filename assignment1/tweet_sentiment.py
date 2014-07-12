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

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = load_scores(sent_file)

    #lines(tweet_file)

    with tweet_file:
        for line in tweet_file:
            message = json.loads(line)
            if 'text' in message:
                tweet_text = message['text']
                score = compute_score(tweet_text, scores)
                print score

if __name__ == '__main__':
    main()
