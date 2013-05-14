import sys
import json

def get_dict(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def hw(sent_file, tweet_file):
    scores = get_dict(sent_file)
    for line in tweet_file:
        raw_tweet = json.loads(line)
        tweet_text = raw_tweet["text"]
        print get_sentiment(tweet_text, scores)

def get_sentiment(sentence, scores):
    numeric_score = 0.0
    for word in sentence.split(" "):
        if(word in scores.keys()):
            numeric_score += scores[word]
    return numeric_score


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
