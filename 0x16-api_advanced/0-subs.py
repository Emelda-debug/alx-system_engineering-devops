#!/usr/bin/python3
"""function that hat queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers
    """
    sub_url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'User-Agent'}
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    subscriber_num = response.json().get('data').get('subscribers')
    return subscriber_num
