#!/usr/bin/python3
"""Querying Reddit"""

import requests


def number_of_subscribers(subreddit):
    """Queries a subreddit and retrieves no. of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'My user Agent 1.0'
    }

 response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # parse JSON response to extract no of subscribers
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
