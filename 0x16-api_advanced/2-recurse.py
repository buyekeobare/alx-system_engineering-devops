#!/usr/bin/python3
"""
Contains the recursive function
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles 
    of all hot articles for a given subreddit. 
    If no results are found for the given subreddit, it returns None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "project:0x16-api_advanced:\
v1.0.0"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    try:
        results = response.json().get("data")
    except ValueError:
        return None

    after = results.get("after")
    children = results.get("children", [])
    for child in children:
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
