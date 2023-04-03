import requests
import config
from twitch_auth import get_twitch_oauth_token

def get_clips(user_id):
    oauth_token = get_twitch_oauth_token()
    headers = {
        "Client-ID": config.TWITCH_ID,
        "Authorization": f"Bearer {oauth_token}"
    }

    url = f"https://api.twitch.tv/helix/clips?broadcaster_id={user_id}"
    response = requests.get(url, headers=headers)
    clip_data = response.json()

    if "data" in clip_data:
        return clip_data["data"]
    else:
        return None

if __name__ == "__main__":
    # Replace with the channel name you want to test
    channel_name = "example_channel"

    # Test the get_stream_info function
    stream_info = get_clips("73437396")
    print(stream_info)
