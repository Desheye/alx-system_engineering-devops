#!/usr/bin/python3
"""
Function to retrieve the number of subscribers for a given subreddit via the Reddit API.
If the subreddit is invalid, return 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    try:
        headers = {'User-Agent': 'My User Agent 1.0'}
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print("An error occurred:", e)
        return 0
