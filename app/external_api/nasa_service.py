import requests

NASA_URL = "https://eonet.gsfc.nasa.gov/api/v3/events"


def fetch_nasa_events():

    try:

        response = requests.get(
            NASA_URL,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("events", [])

    except Exception as e:

        print(f"NASA API Error: {e}")

        return []