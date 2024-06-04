#!/usr/bin/python3
"""
This module provides a function to count the occurrences of words from
a given word list in the titles of the hot posts of a subreddit.
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Count the occurrences of words from a given word list in the titles of the hot posts of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to count.
        after (str, optional): The 'after' parameter for pagination. Defaults to None.
        word_count (Counter, optional): A Counter object to store the word counts. Defaults to None.

    Returns:
        None

    Raises:
        None
    """
    if word_count is None:
        word_count = Counter()

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            if not posts and not word_count:
                return
            
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    word_lower = word.lower()
                    word_count[word_lower] += title.split().count(word_lower)
            
            after = data.get('data', {}).get('after')
            if after:
                count_words(subreddit, word_list, after, word_count)
            else:
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    if count > 0:
                        print(f'{word}: {count}')
                if not sorted_word_count:
                    return
        else:
            return
    except requests.RequestException:
        return
