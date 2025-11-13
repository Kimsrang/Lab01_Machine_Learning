"""
ingest.py
----------
Loops through dates to fetch and save data (Bronze layer).
"""

from datetime import date, timedelta
from src.rte_forecast.get_forecast import fetch_generation_forecast, save_forecast_json

def ingest_all_data(start_date=date(2020,1,1), end_date=date.today()):
    current = start_date
    while current <= end_date:
        date_str = current.strftime("%Y-%m-%d")
        try:
            data = fetch_generation_forecast(date_str, date_str)
            save_forecast_json(data, date_str)
        except Exception as e:
            print(f"❌ Error fetching {date_str}: {e}")
        current += timedelta(days=1)
    print("✅ Ingestion complete.")


if __name__ == "__main__":
    ingest_all_data()
