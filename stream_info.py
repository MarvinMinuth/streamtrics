import requests
import config
from twitch_auth import get_twitch_oauth_token


def get_stream_info(channel_name):
    # Get the OAuth token
    access_token = get_twitch_oauth_token()

    # Define the Twitch API endpoint for getting stream information
    api_url = f"https://api.twitch.tv/helix/streams?user_login={channel_name}"

    # Set up the request headers with the client ID and access token
    headers = {
        "Client-ID": config.TWITCH_ID,
        "Authorization": f"Bearer {access_token}",
    }

    # Send the API request
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Error fetching stream info: {response.text}")

    # Parse the JSON response
    stream_data = response.json()["data"]

    # Check if the stream is live
    if len(stream_data) == 0:
        return None

    # Extract the stream information
    stream_info = stream_data[0]

    # Return the stream information
    return stream_info

