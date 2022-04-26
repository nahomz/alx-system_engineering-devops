#!/usr/bin/python3
"""A script that gets top ten articles for a subreddit"""
import json
import requests


def top_ten(subreddit):
    """Function that requests the top ten articles for a subreddit"""

    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "com.holbertonschool.myredditscript:0.0.1"
    params = {'limit': 10}
    headers = {'user-agent': user_agent}
    r = requests.get(URL, headers=headers, params=params)
    if (r.status_code is not 200):
        print('None')
        return
    r = r.json()
    posts = r['data']['children'][0:10]
    if len(posts) is 0:
        print('None')
        return
    for post in posts:
        print(post['data']['title'])
