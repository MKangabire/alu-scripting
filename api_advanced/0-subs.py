#!/usr/bin/python3
"""
uses reddit's APIs
to get the number of total number of subscribers
of a subrredit
"""


import json
import requests
import sys


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers of a given subrredit
    """
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
            "User-Agent": "0-subs/1.0"
    }

    raw_response = requests.get(URL, headers=headers)

    if (raw_response.status_code) == 200:
        json_response = raw_response.json()
        sub_count = json_response['data']['subscribers']
        return sub_count

    else:
        return 0

if __name__ == "__main__":
    pass
