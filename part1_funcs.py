'''
Hope Tambala
25677464
'''

# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# Support Functions 
def store_tweet_text(new_tweets):
    #List comprehension
    #tweets = [[tweet.full_text] for tweet in new_tweets]
    tweets = []
    for tweet in new_tweets:
        tweets.append(tweet.full_text)

    #print (str(tweets))
    return (str(tweets))