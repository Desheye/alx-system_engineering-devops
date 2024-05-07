#!/usr/bin/python3
import requests

"""
Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit.
"""


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0


print(number_of_subscribers("python"))
