import requests
import config

def get_twitch_oauth_token():

    url = "https://id.twitch.tv/oauth2/token"
    payload = {
        "client_id": config.TWITCH_ID,
        "client_secret": config.SECRET_KEY,
        "grant_type": "client_credentials"
    }
    
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data["access_token"]
        return access_token
    else:
        print(f"Error while fetching OAuth token: {response.status_code}, {response.text}")
        return None