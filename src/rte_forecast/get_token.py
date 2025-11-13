"""
get_token.py
-------------
Handles authentication to the RTE France API.
Fetches and returns a valid OAuth token.
"""

import requests
import os

def get_token():
    url = "https://digital.iservices.rte-france.com/token/oauth/"
    payload = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("RTE_CLIENT_ID"),
        "client_secret": os.getenv("RTE_CLIENT_SECRET")
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    token = response.json().get("access_token")

    # Optionally save token to Bronze folder
    os.makedirs("data/bronze", exist_ok=True)
    with open("data/bronze/token.txt", "w") as f:
        f.write(token)

    print("✅ Token fetched and saved to data/bronze/token.txt")
    return token


if __name__ == "__main__":
    get_token()
