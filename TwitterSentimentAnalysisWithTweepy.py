import tweepy
from textblob import TextBlob

CONSUMER_API_KEY = '<Your Value From Twitter account>'
CONSUMER_API_SECRET = '<Your Value From Twitter account>'

ACCESS_TOKEN = '<Your Value From Twitter account>'
ACCESS_TOKEN_SECRET = '<Your Value From Twitter account>'

auth = tweepy.OAuthHandler(consumer_api_key, CONSUMER_API_SECRET)
auth.set_ACCESS_TOKEN(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.search(raw_input("Please enter topic of interest to search related tweets : "))

for tweet in public_tweets:
	print (tweet.text)
	analysis = TextBlob(tweet.text)
	print (analysis.sentiment)