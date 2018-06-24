'''
Hope Tambala
25677464
'''

# these should be the only imports you need
import tweepy
import nltk
import json
import sys
import csv

from part1_funcs import *


# write your code here
# usage should be python3 part1.py <username> <num_tweets>

# Consumer keys and access tokens, used for OAuth
# Developer Twitter Account Credentials
consumer_key = '5Ni3RwVjuyntkTW2PSsTbvjeA'
consumer_secret = 'K4VVQ6Q7jUt8mqydmHExyFNFt4bCL8xjjb0TysVxECXjzYsmsN'
access_token = '1008535087795798016-E1NRr7zRFUGvz84nnHAESjCp2OR7XY'
access_token_secret = 'JPwTUaQUB68lI639mQcvXCt4CvCntBoSOlC8sSWpthSKy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Params
'''
screen_name = sys.argv[1]
number2analyze = int(sys.argv[2])

'''
screen_name = 'tRUbLU911'
number2analyze = 100


#---*
user = api.get_user(screen_name)

#Main Functions 
def print_username(user):
    print ('UMSI: '+ user.screen_name);
def tweets_analyzed(user):
    print ('TWEETS ANALYZED: ' + str(user.statuses_count));
def verbs(tagged):
    arr5 = []

    word_tag_fd = FreqDist(tagged)
    for word, frequency in word_tag_fd.most_common():
        #print(u'{}({})'.format(word[0], frequency))
        if word[1] =='VB':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
        elif word[1] =='VBD':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
        elif word[1] =='VBN':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
        elif word[1] =='VBP':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
        elif word[1] =='VBG':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
        elif word[1] =='VBZ':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)

   
    '''
    #Works for just listing verbs
    print ([wt[0] for (wt, freq) in word_tag_fd.most_common() if wt[1] == 'VB'])
    '''

    '''
    #Works for Entire list
    for word, frequency in word_tag_fd.most_common(5):
        #print(u'{}({})'.format(word[0], frequency))
        miniString = u'{}({})'.format(word[0], frequency) + ' '
        stringOf5 += miniString
    '''
    #print ('VERBS: ' + str(arr5[:5]))
    print ('VERBS: ' + ''.join(arr5[:5]))
def nouns(tagged):
    arr5 = []

    word_tag_fd = FreqDist(tagged)
    for word, frequency in word_tag_fd.most_common():
        #print(u'{}({})'.format(word[0], frequency))
        if word[1] =='NN':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
        elif word[1] =='NNS':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
        elif word[1] =='NNP':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
        elif word[1] =='NNPS':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
    

    print ('NOUNS: ' + ''.join(arr5[:5]))

    
    nounFile = arr5
    nounFile.insert(0, ("Noun", "Number"))
    file2write2 = open('noun_data.csv', 'w')
    with file2write2:
        writer = csv.writer(file2write2)
        '''
        writer.writerows(nounFile)
        '''
        for val in nounFile:
            writer.writerow([val])

def adjectives(tagged):
    arr5 = []

    word_tag_fd = FreqDist(tagged)
    for word, frequency in word_tag_fd.most_common():
        #print(u'{}({})'.format(word[0], frequency))
        if word[1] =='JJ':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
        elif word[1] =='JJR':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)
        elif word[1] =='JJS':
            miniString = u'{}({})'.format(word[0], frequency) + ' '
            arr5.append(miniString)

    print ('ADJECTIVES ' + ''.join(arr5[:5]))

'''
def original_tweets():
    print
def times_favorited():
    print
def times_retweeted():
    print
def write2file(nouns):
    print
'''

new_tweets = api.user_timeline(screen_name = screen_name, count = number2analyze, tweet_mode="extended")


#Main
print_username(user);
tweets_analyzed(user);

verbs(pos_tagger(return_tokenize(store_tweet_text(new_tweets))));
nouns(pos_tagger(return_tokenize(store_tweet_text(new_tweets))));
adjectives(pos_tagger(return_tokenize(store_tweet_text(new_tweets))));
