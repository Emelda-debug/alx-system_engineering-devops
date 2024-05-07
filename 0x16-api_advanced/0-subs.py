"""
Function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers.
    """
    headers = {'User-Agent': 'My-User-Agent'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    data = response.json().get('data', {})
    subscriber_num = data.get('subscribers', 0)
    return subscriber_num
