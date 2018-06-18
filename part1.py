'''
Hope Tambala
25677464
'''

# these should be the only imports you need
import tweepy
import nltk
import json
import sys

from part1_funcs import *


from nltk.tokenize import sent_tokenize, word_tokenize



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
screen_name = 'tRUbLU911'
number2analyze = 5


#---*
user = api.get_user(screen_name)

#Main Functions 
def print_username(user):
    print ('UMSI: '+ user.screen_name);
def tweets_analyzed(user):
    print ('TWEETS ANALYZED: ' + str(user.statuses_count));
def verbs(tweets):
    tweetsArray = store_tweet_text(tweets); 
    print (tweetsArray)
def nouns():
    print
def adjectives():
    print
def original_tweets():
    print
def times_favorited():
    print
def times_retweeted():
    print


'''
Source
https://stackoverflow.com/questions/42705314/getting-full-tweet-text-from-user-timeline-with-tweepy
'''
new_tweets = api.user_timeline(screen_name = screen_name, count = number2analyze, tweet_mode="extended")



print_username(user);
tweets_analyzed(user);

'''
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
'''
'''
print (user.followers_count);
for friend in user.friends():
   print (friend.screen_name);

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
'''