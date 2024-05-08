#!/usr/bin/python3
import requests

"""
Write a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print("No posts found.")
            else:
                for post in posts:
                    print(post['data']['title'])
        else:
            print("Failed to retrieve data from Reddit.")
    except requests.RequestException as e:
        print("An error occurred:", e)


# Example usage:
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
