#!/usr/bin/python3
"""Module that produces a function that returns number of subscribers"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.

    If the subreddit does not exist, it returns 0.

    Parameters:
    subreddit (str): The subreddit to fetch the subscriber count for.

    Returns:
    int: The number of subs
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0
