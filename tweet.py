#!/usr/bin/env python3

# import libraries
import os
import sys
import requests
import re
PATH='/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages'
sys.path.insert(1, PATH)
import tweepy
from datetime import date

# Twitter Credentials
consumer_key = '7K1swuCZ97lda6Z1SRP7I0DPE'
consumer_secret = 'yK0TaK3SmqZqB7H54kY49n3wCmeSuPnGnIrVn8HjkYnAsCr6Xw'
access_token = '1511749526213832710-5N9pLxVr9dLHaqv4HHubnVCG9t3bbd'
access_token_secret = 'fOIpOCUZDJCZIxoboXhl8DBrruMc3UMZ3CHIvVREhPRCg'

# Constants
FILE = 'floridaman.txt'
today = date.today()

# Month
month = today.strftime("%B")

# Day
day = today.strftime("%d")

# Functions

def checkdate(day):
    
    zeros = []
    for num in day:
        zeros.append(num)
    if zeros[0] == '0': 
        zeros.pop(0)
        day = zeros[0]
        print(day)


def readfile(FILE):

    with open(FILE, "r") as file:
        pattern = month + ' ' + day
        for line in file:
            if re.search(pattern, line):
                tweet = line.split(':', 1)


# if __name__ == "__main__":

  #  def main():

# Check Date
checkdate(day)
print(day)
#  Make Tweet
readfile(FILE)
# Print 
print(f'Today, {month} {day}, in {tweet}', end = ' ')   



'''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

api.create_friendship(screen_name='griffinlaszlo')
'''
