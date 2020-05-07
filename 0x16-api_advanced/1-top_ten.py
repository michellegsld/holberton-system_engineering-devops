#!/usr/bin/python3
"""
Task 1:
Queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit
If a subreddit is invalid then it prints None
1-top_ten.py
"""
import requests


def top_ten(subreddit):
    """
    Returns:
    Number of subscribers to a subreddit
    or 0 on invalid subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    param = {'limit': 10}
    head = {'user-agent': 'michellegsld-holberton'}
    req = requests.get(url, params=param, headers=head, allow_redirects=False)
    try:
        for num in range(0, 10):
            print(req.json()['data']['children'][num]['data']['title'])
    except:
        print(None)
