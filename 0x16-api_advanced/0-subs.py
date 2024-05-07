#!/usr/bin/python3

"""
Retrieve the number of subscribers for a given subreddit via the Reddit API.
If the subreddit is invalid, return 0.
"""

import json
import requests
import sys

# Define user agent
user_agent = {
    'User-Agent': 'My User Agent 1.0'
}


def get_subscribers_count(subreddit):
    """Return the subscriber count of a subreddit."""
    try:
        url = 'https://www.reddit.com/r/'
        response = requests.get(url + subreddit + "/about.json",
                                headers=user_agent, allow_redirects=False)
        return response.json()['data']['subscribers']
    except:
        return 0
