#!/usr/bin/python3
"""
Task 2:
Queries the Reddit API and returns a list containing
titles of all hot articles for a given subreddit
If a subreddit is invalid then it returns None
2-recurse.py
"""
import requests


def recurse(subreddit, hot_list=[], child=0):
    """
    Returns:
    List of all hot titles in a subreddit
    Or None if the subreddit is invalid
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    head = {'user-agent': 'michellegsld-holberton'}
    req = requests.get(url, headers=head, allow_redirects=False)

    try:
        hot_list.append(req.json()['data']['children'][child]['data']['title'])
    except:
        return None

    recurse(subreddit, hot_list, child=child+1)
    return hot_list
