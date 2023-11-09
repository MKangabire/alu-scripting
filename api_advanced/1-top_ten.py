#!/usr/bin/python3
"""
a function print the titles of the first 10 hot posts listed for a given subreddit.
"""

import json
import requests
import sys

def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    """
    URL = "https://www.reddit.com/r/{}/top.json".format(subreddit)

    headers = {"User-Agent": "0-subs/2.0"}

    response = requests.get(URL, headers=headers)

    if (response.status_code) == 200:
        sys.stdout.write("OK")

    else:
        print("error")
