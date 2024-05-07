#!/usr/bin/python3
import requests

"""
Write a recursive function that queries the Reddit API
Parses the title of all hot articles, and prints a sorted count of
given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""


def count_words(subreddit, word_list, after=None, word_count={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if ' ' + word.lower() + ' ' in title \
                            or title.startswith(word.lower() + ' ') \
                            or title.endswith(' ' + word.lower()) \
                            or title == word.lower():
                        word_count[word.lower()] = word_count.get(
                            word.lower(), 0) + 1

            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                sorted_word_count = sorted(
                    word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")
        else:
            print("No results found or invalid subreddit.")
    except requests.RequestException:
        print("No results found or invalid subreddit.")


# Example usage:
count_words("python", ["python", "java", "javascript"])
