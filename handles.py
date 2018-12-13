# Import Dependencies
import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

def get_handles():
    # Grabbing twitter handles to pass to analyzer 
    me = 'tjg_developer'

    tweets = api.search(f'@{me} Analyze:')['statuses']

    requests = tweets[0]['entities']['user_mentions']

    handles = []

    # Collect all screen names in user_mentions that are not 'me'
    for request in requests:
        if request['screen_name'] != me:
            handles.append('@' + request['screen_name'])
        else:
            pass
    
    return handles