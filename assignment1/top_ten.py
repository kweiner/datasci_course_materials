import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])

    hashtag_counts = {}

    with tweet_file:
        for line in tweet_file:
            message = json.loads(line)
            if 'entities' in message:
                entities = message['entities']
                if 'hashtags' in entities:
                    hashtags = entities['hashtags']
                    if hashtags:
                        for hashtag in hashtags:
                            text = hashtag['text']
                            hashtag_counts[text] = hashtag_counts.get(text, 0) + 1

    top10 = sorted(hashtag_counts.items(), key=lambda x:x[1], reverse=True)[:10]
    for tag in top10:
        print tag[0],tag[1]

if __name__ == '__main__':
    main()
