#!/usr/bin/env python3

# import libraries
import os
import sys
import tweepy
import credentials
import re
from datetime import date
import json

# Create client 
client = tweepy.Client(
    consumer_key=credentials.consumer_key, 
    consumer_secret=credentials.consumer_secret,
    access_token=credentials.access_token, 
    access_token_secret=credentials.access_token_secret
)

# Constants
# FILE = 'floridaman.txt' # change to json
# FILE = 'tweets.json'
today = date.today()

# Month
month = today.strftime("%B") # stays the same

# Day
day = today.strftime("%d") # stays the same

# Main

zeros = []
for num in day:
    zeros.append(num)
if zeros[0] == '0': 
    zeros.pop(0)
    day = zeros[0]

FILE = open('tweets.json')
tweets = json.load(FILE)

# with open(FILE, "r") as file:
for key, value in tweets.items():
    pattern = month + ' ' + day
    length = len(key)
    date = key[:length-6]
    headline = None
    link = None
    if date == pattern:
        year = key[-4:]
        headline = tweets[key][0]
        link = tweets[key][1]
        tweet = (f'Today, {month} {day}, in {year}: {headline}\n\nFull article: {link}')
        break

# Create Tweet
response = client.create_tweet(text=tweet)
print(f"https://twitter.com/user/status{response.data['id']}")
print(f"Tweet that was sent: ")
print(tweet)


