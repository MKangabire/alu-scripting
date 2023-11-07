#!/usr/bin/python3
"""
Reddit API Subreddit Subscribers Query Module

This module defines a function that queries the
Reddit API to retrieve the number of subscribers
for a given subreddit.

"""
import json
import requests

def number_of_subscribers(subreddit):
    """
    Write a function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.

    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Create a custom user agent
    headers = {'User-Agent': 'OboloScript/1.0'}
    
    try:
        # Send a GET request to the URL with custom headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception if the request fails

        # Decode the JSON response
        res_json = response.json()
    except requests.exceptions.RequestException:
        return 0
    else:
        return res_json["data"]["subscribers"]

