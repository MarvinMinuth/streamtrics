import requests
import config
from twitch_auth import get_twitch_oauth_token

def get_follower_stats(user_id):
    oauth_token = get_twitch_oauth_token()
    headers = {
        "Client-ID": config.TWITCH_ID,
        "Authorization": f"Bearer {oauth_token}"
    }

    url = f"https://api.twitch.tv/helix/users/follows?to_id={user_id}"
    response = requests.get(url, headers=headers)
    follower_data = response.json()

    if "total" in follower_data:
        return follower_data["total"]
    else:
        return None

