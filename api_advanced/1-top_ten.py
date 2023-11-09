#!/usr/bin/python3
"""
a function print the titles of the first 10 hot posts listed for a given subreddit.
"""

import json
import requests

def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    """
    URL = "https://www.reddit.com/r/{}/top.json".format(subreddit)

    headers = {"User-Agent": "0-subs/2.0"}

    response = requests.get(URL, headers=headers)

    if (response.status_code) == 200:
        json_response = response.json()

        sorted_posts = sorted(json_response['data']['children'], key=lambda x: x['data']['score'], reverse=True)

        for post in sorted_posts[:10]:
            title = post['data']['title']
            print(title)
i
        else:
            print("error")
