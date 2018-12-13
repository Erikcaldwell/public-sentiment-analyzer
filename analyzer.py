# Import Dependencies
import pandas as pd
import tweepy
import numpy as np
import time
import os
import requests
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']
api_key = os.environ['api_key']
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from handles import get_handles

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

def analyzer():
    handles = get_handles()
    data = []
    # Grab twitter handles and append the name and image to data
    for handle in handles:
        data_dict = {}
        tweets = api.user_timeline(handle)
        data_dict['Handle'] = handle
        data_dict['Name'] = tweets[0]['user']['name']
        data_dict['Image'] = tweets[0]['user']['profile_image_url_https'].replace('normal', '400x400')
        data.append(data_dict)

    # Setup sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Grab tweets containing the user name of the twitter handle
    for user in data:
        compound_scores = []
        tweets = api.search_users(user['Name'])
        query_name = user['Name']
        articles = requests.get('https://newsapi.org/v2/everything?q=' + query_name + '&language=en' + "&apiKey=" + api_key).json()

        # Run sentiment analysis on tweets and append the average
        # compound sentiment score to data
        for tweet in tweets:
            try:
                sent = analyzer.polarity_scores(tweet['status']['text'])
                compound_scores.append(sent['compound'])
            except KeyError:
                pass

        for article in articles['articles']:
            if article['content']:
                senti = analyzer.polarity_scores(article["content"])
                compound_scores.append(senti['compound'])

        user['Score'] = np.mean(compound_scores)

    # Convert the list of dictionaries to a dataframe
    data_df = pd.DataFrame(data)

    # Sort the dataframe by Score in descending order
    data_df_sorted = data_df.sort_values(by='Score', ascending=False)

    # Convert the dataframe back to a list of dictionaries
    data_ordered = data_df_sorted.to_dict('records')

    return data_ordered
