import requests
import config
from twitch_auth import get_twitch_oauth_token

def get_user_info(username):
    oauth_token = get_twitch_oauth_token()
    headers = {
        "Client-ID": config.TWITCH_ID,
        "Authorization": f"Bearer {oauth_token}"
    }

    url = f"https://api.twitch.tv/helix/users?login={username}"
    response = requests.get(url, headers=headers)
    user_data = response.json()

    if "data" in user_data and len(user_data["data"]) > 0:
        return user_data["data"][0]
    else:
        return None


def get_user_id(username):
    return get_user_info(username)["id"]
