'''
Hope Tambala
25677464
'''

# these should be the only imports you need
import tweepy
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist

import json
import sys

# Support Functions 
def store_tweet_text(new_tweets):
    '''
    List comprehension
    tweets = [[tweet.full_text] for tweet in new_tweets]
    '''
    '''
    Array Append
    tweets = []
    for tweet in new_tweets:
        tweets.append(tweet.full_text)
    '''
    tweets = ''
    for tweet in new_tweets:
        tweets += tweet.full_text

    #print (str(tweets))
    return (tweets)

def return_tokenize(data):
    #tokens = data
    stopWords = set(stopwords.words('english'))
    newStopWords = ['http', 'https','RT',';','.',':','!','+',',','?','/','$','#','@','``','...']
    stopWords.update(newStopWords)  


    tokens = word_tokenize(data)

    # Remove single-character tokens (mostly punctuation)
    tokens = [word for word in tokens if len(word) > 1]

    # Remove numbers
    tokens = [word for word in tokens if not word.isnumeric()]

    tokens = [word for word in tokens if word[0].isalpha()]
    

    #Array of Filtered Worlds
    filteredWords = []

    for t in tokens:
        if t not in stopWords:
            filteredWords.append(t)

    return filteredWords

def pos_tagger(tokens):
    #tagged = tokens
    tagged = nltk.pos_tag(tokens)
    
    #print (tagged)
    return tagged   
    '''
    fdist = FreqDist(tagged)
    return fdist
    '''
    '''
    for word, frequency in fdist.most_common(5):
        #print(u'{};{}'.format(word, frequency))
        print(word,frequency)
    '''    
