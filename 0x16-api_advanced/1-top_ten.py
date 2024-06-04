#!/usr/bin/python3
"""Module that represents a function to return top 10 posts"""
import requests


def top_ten(subreddit):
    """
    Function that prints the first 10 hot posts listed for 
    a given subreddit
    subreddit: the given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozzila/5.0'}

    try:
        response = requests.get(url, headers= headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            if posts:
                for post in posts:
                    print(post['data']['title'])
            else:
                print(None)
        else:
            print(None)
    except resuests.ResuestException as e:
        print(None)
