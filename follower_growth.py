import requests
import config
from datetime import datetime, timedelta
from twitch_auth import get_twitch_oauth_token
from user_info import get_user_id

def get_follower_growth(username, period='daily' ):
    user_id = get_user_id(username)
    if not user_id:
        return None

    access_token = get_twitch_oauth_token()
    if not access_token:
        return None

    headers = {
        'Client-ID': config.TWITCH_ID,
        'Authorization': f'Bearer {access_token}'
    }


    url = f'https://api.twitch.tv/helix/users/follows?to_id={user_id}&first=100'
    response = requests.get(url, headers=headers)
    data = response.json()

    if 'data' not in data:
        return None

    followers = data['data']
    follower_growth = {}

    for follower in followers:
        followed_at = datetime.strptime(follower['followed_at'], '%Y-%m-%dT%H:%M:%SZ')
        now = datetime.utcnow()

        if period == 'daily':
            time_diff = (now - followed_at).days
        elif period == 'weekly':
            time_diff = (now - followed_at).days // 7
        elif period == 'monthly':
            time_diff = (now - followed_at).days // 30

        if time_diff in follower_growth:
            follower_growth[time_diff] += 1
        else:
            follower_growth[time_diff] = 1
    pagination_cursor = data['pagination']['cursor']

    while pagination_cursor:
        url = f'https://api.twitch.tv/helix/users/follows?to_id={user_id}&first=100&after={pagination_cursor}'
        response = requests.get(url, headers=headers)
        data = response.json()

        if 'data' not in data:
            return None

        followers = data['data']

        for follower in followers:
            followed_at = datetime.strptime(follower['followed_at'], '%Y-%m-%dT%H:%M:%SZ')
            now = datetime.utcnow()

            if period == 'daily':
                time_diff = (now - followed_at).days
            elif period == 'weekly':
                time_diff = (now - followed_at).days // 7
            elif period == 'monthly':
                time_diff = (now - followed_at).days // 30

            if time_diff in follower_growth:
                follower_growth[time_diff] += 1
            else:
                follower_growth[time_diff] = 1
        pagination_cursor = data['pagination']['cursor']

    return follower_growth

if __name__ == "__main__":
    username = "Bonjwa"

    growth = get_follower_growth(username, period='daily')
    print(f"Follower growth for {username}: {growth}")
