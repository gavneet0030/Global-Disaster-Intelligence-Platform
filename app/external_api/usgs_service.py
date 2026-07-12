import requests

USGS_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
)


def fetch_earthquakes():

    try:

        response = requests.get(
            USGS_URL,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("features", [])

    except Exception as e:

        print(f"USGS API Error: {e}")

        return []