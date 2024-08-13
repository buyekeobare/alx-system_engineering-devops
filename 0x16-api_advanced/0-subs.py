#!/usr/bin/python3
"""Querying Reddit"""

import requests


def number_of_subscribers(subreddit):
    """Queries a subreddit and retrieves no of subscribers"""

    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid too many request errors
    headers = {'User-Agent': 'MyRedditApp/1.0 (by /u/byekeobare)'}

    # send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and not redirected
    if response.status_code == 200:
        # parse JSON response to extract no of subscribers
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
