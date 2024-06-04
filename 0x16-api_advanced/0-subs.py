#!/usr/bin/python3
"""Module that produces a function that returns number of subscribers"""
import requests
import json


def number_of_subscribers(subreddit):
    """
    Function to return the number of subscribers for a given subreddit
    if the subredit does not exist, it returns 0
    subredit: the subredit to to fetch
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0
