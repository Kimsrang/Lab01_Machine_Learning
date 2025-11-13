"""
get_forecast.py
----------------
Fetches D-1 generation forecast data from RTE API
and saves it to the Bronze folder as JSON files.
"""

import requests, json, os
from datetime import datetime
from src.rte_forecast.get_token import get_token

def fetch_generation_forecast(start_date, end_date):
    url = "https://digital.iservices.rte-france.com/open_api/generation_forecast/v3/generation_forecast"
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "start_date": f"{start_date}T00:00:00Z",
        "end_date": f"{end_date}T23:59:59Z",
        "type": "D-1"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    print(f"✅ Data fetched for {start_date}")
    return data


def save_forecast_json(data, date_str):
    year, month, day = date_str.split("-")
    save_dir = f"data/bronze/{year}/{month}"
    os.makedirs(save_dir, exist_ok=True)
    path = f"{save_dir}/{day}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"💾 Saved JSON: {path}")


if __name__ == "__main__":
    today = datetime.today().strftime("%Y-%m-%d")
    data = fetch_generation_forecast(today, today)
    save_forecast_json(data, today)
