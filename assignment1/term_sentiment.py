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
    scores_all = {}
    for line in tweet_file:
        raw_tweet = json.loads(line)
        tweet_text = raw_tweet["text"]
        sentiment = get_sentiment(tweet_text, scores)
        for word in tweet_text.split(" "):
            if(word in scores.keys()):
                scores_all[word] = scores[word]
            else:
                if(word in scores_all.keys()):
                    old_score = scores_all[word]
                    new_score = (old_score + sentiment)/2.0
                    scores_all[word] = new_score
                else:
                    scores_all[word] = sentiment
    display_scores(scores_all)


def display_scores(dict):
    for key in dict.keys():
        print key, dict[key]


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

