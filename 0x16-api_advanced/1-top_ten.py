#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
If the subreddit is invalid or there are no posts, prints None.
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    try:
        base_url = 'https://www.reddit.com/r/'
        response = requests.get(base_url + subreddit + "/hot.json?limit=10",
                                headers={'User-Agent': 'imgn-drgn'}, allow_redirects=False)
        titles = [post['data']['title'] for post in response.json()['data']['children']]
        print(*titles, sep='\n')
    except:
        print(None)

# Example usage:
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
