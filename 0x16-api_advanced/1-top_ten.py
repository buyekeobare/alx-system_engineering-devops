#!/usr/bin/python3
"""Querying subreddit"""

import requests


def top_ten(subreddit):
    """Query Reddit and print titles of the first 10 hot posts"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User Agent to avoid too many request errors
    headers = {'User-Agent': 'MyRedditApp/1.0 (by /u/buyekeobare)'}

    # send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
