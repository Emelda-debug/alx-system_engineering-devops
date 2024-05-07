#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the top 10 hot posts
    """
    headers = {'User-Agent': 'My-User-Agent'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print('None')
    else:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            title = post.get('data', {}).get('title')
            print(title)
