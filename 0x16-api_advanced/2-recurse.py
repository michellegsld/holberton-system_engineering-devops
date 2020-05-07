#!/usr/bin/python3
"""
Task 2:
Queries the Reddit API and returns a list containing
titles of all hot articles for a given subreddit
If a subreddit is invalid then it returns None
2-recurse.py
"""
import requests


def recurse(subreddit, hot_list=[], param={}):
    """
    Returns:
    List of all hot titles in a subreddit
    Or None if the subreddit is invalid
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    head = {'user-agent': 'michellegsld-holberton'}
    req = requests.get(url, params=param, headers=head, allow_redirects=False)

    try:
        for child in range(0, req.json()['data']['dist']):
            post = req.json()['data']['children'][child]['data']['title']
            hot_list.append(post)
        param['after'] = req.json()['data']['after']
    except:
        return None

    recurse(subreddit, hot_list, param)
    return hot_list
