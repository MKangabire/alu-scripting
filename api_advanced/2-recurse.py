#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot
articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import json
import time
import urllib.error
import urllib.parse
import urllib.request


def recurse(subreddit, hot_list=[]):
    list_len = len(hot_list)
    limit = list_len + 1
    query = {"limit": limit - 1}
    query = urllib.parse.urlencode(query)
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?{query}"
    req_object = urllib.request.Request(url, method="GET")
    req_object.add_header('User-Agent', 'OboloScript/3.0')
    try:
        with urllib.request.urlopen(req_object) as resp_object:
            resp_json = json.load(resp_object)
    except urllib.error.HTTPError:
        return None
    else:
        resp_children = resp_json["data"]["children"]
        try:
            _ = resp_children[limit - 1]["data"]["title"]
        except IndexError:
            return hot_list
        else:
            if len(resp_children) == 2:
                hot_list.append(resp_children[limit - 1]["data"]["title"])
                hot_list.append(resp_children[limit]["data"]["title"])
                """
                or this below
                final_list.append(0)
                final_list.append(1)
                hot_list += "0"
                hot_list += "1"
                """
            else:
                hot_list.append(resp_children[limit - 1]["data"]["title"])
                """
                or this below
                final_list.append(2)
                hot_list += "2"
                """
                time.sleep(5)
            return recurse(subreddit, hot_list)
