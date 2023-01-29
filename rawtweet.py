#!/usr/bin/env python3

# import libraries
import os
import sys
import requests
import re
import tweepy
import credentials
from datetime import date

# Create client 
client = tweepy.Client(
    consumer_key=credentials.consumer_key, 
    consumer_secret=credentials.consumer_secret,
    access_token=credentials.access_token, 
    access_token_secret=credentials.access_token_secret
)

# Constants
FILE = 'floridaman.txt' # change to json
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

with open(FILE, "r") as file:
    pattern = month + ' ' + day
    for line in file:
        if re.search(pattern, line):
            tweet = line.split(':', 1)

# Create Tweet
# print(f'Today, {month} {day}, in {tweet[1]}', end = ' ')
tweet = tweet[1]
one="Today, "
four=", in"
space=' '
response = client.create_tweet(
    text=one+month+space+day+four+tweet
)
print(f"https://twitter.com/user/status{response.data['id']}")
print(f"Tweet that was sent: ")
print(f'Today, {month} {day}, in {tweet}', end = ' ')


