import requests

USGS_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
)


def get_live_earthquakes():
    response = requests.get(USGS_URL, timeout=10)

    if response.status_code != 200:
        return []

    data = response.json()

    earthquakes = []

    for item in data.get("features", []):

        properties = item.get("properties", {})
        geometry = item.get("geometry", {})

        coordinates = geometry.get("coordinates", [None, None, None])

        earthquakes.append(
            {
                "id": item.get("id"),
                "place": properties.get("place"),
                "magnitude": properties.get("mag"),
                "time": properties.get("time"),
                "latitude": coordinates[1],
                "longitude": coordinates[0],
                "depth": coordinates[2],
            }
        )

    return earthquakes