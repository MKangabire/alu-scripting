#!/usr/bin/python3
"""
prints the titles of
the first 10 hot posts listed
for a given subreddit.
"""


import json
import requests
import sys


def top_ten(subreddit):
    """
    prints 10 hot posts
    """
    URL = "https://www.reddit.com/r/{}/Hot.json".format(subreddit)
    headers = {
            "User-Agent": "1-top_ten/1.0"
    }

    response = requests.get(URL, headers=headers)

    if (response.status_code) == 200:
        json_response = response.json()
        titles = json_response['data']['top_ten']
        return titles

    else:
        print('None')

if __name__ == '__main__':
    pass
