__author__ = "Apurv Verma"
__date__ = "$May 13, 2013"

import urllib
import json

def print_tweets():
    response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
    response_as_json = json.load(response)
    response_headers = response_as_json.keys()
    tweets = response_as_json["results"]
    for i in range(len(tweets)):
            tweet = tweets[i]
            print tweet["text"]

if __name__ == "__main__":
    print_tweets()
