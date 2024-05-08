#!/usr/bin/python3
"""
Queries the Reddit API and returns the total number of subscribers 
for a given subreddit.
If the subreddit is invalid, returns 0.
"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a subreddit."""
    try:
        url = 'https://www.reddit.com/r/'
        response = requests.get(url + subreddit + "/about.json",
                                headers={'User-Agent': 'imgn-drgn'}, allow_redirects=False)
        return response.json()['data']['subscribers']
    except:
        return 0
