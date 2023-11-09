#!/usr/bin/python3
"""
prints OK if ran successful.
"""

import json
import requests
import sys


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    """
    URL = "https://www.reddit.com/r/{}/top.json".format(subreddit)

    params = {
            "t": "all",
            "count": 0,
            "limit": 10
    }

    headers = {"User-Agent": "0-subs/2.0"}

    response = requests.get(URL, params=params, headers=headers)

    if response.status_code == 200:
        resp_json = response.json()
        resp_children = resp_json['data']['top_ten']
        return resp_children 

    else:
        print'(None')

if __main__ == "__main__":
    pass
