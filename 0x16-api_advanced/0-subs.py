import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a subreddit."""
    try:
        client_id = 'wJX6bxt8Y5DPc2Hc-KpKnQ'
        client_secret = '3v5TgPVWRVP1fGcnxrvSyo3ERapVsg'
        username = 'Cancer_TheZodiac'
        password = 'cancerthezodiac'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        data = {'grant_type': 'password', 'username': username, 'password': password}
        headers = {'User-Agent': user_agent}

        response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
        access_token = response.json().get('access_token')

        if access_token:
            headers = {'User-Agent': user_agent, 'Authorization': 'Bearer {}'.format(access_token)}
            url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
            response = requests.get(url, headers=headers, allow_redirects=False)
            return response.json()['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print("Error:", e)
        return 0

# Example usage:
print(number_of_subscribers("programming"))
