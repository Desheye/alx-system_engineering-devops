#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']
            for post in posts:
                hot_list.append(post['data']['title'])
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None


# Example usage:
result = recurse("python")
if result is not None:
    for title in result:
        print(title)
else:
    print("No results found or invalid subreddit.")
