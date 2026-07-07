import requests

NASA_URL = "https://eonet.gsfc.nasa.gov/api/v3/events"


def get_nasa_events():

    response = requests.get(
        NASA_URL,
        timeout=10
    )

    if response.status_code != 200:
        return []

    data = response.json()

    events = []

    for event in data.get("events", []):

        geometry = event.get("geometry", [])

        if len(geometry) == 0:
            continue

        coordinates = geometry[-1].get(
            "coordinates",
            []
        )

        if len(coordinates) < 2:
            continue

        categories = event.get(
            "categories",
            []
        )

        category = "Unknown"

        if len(categories) > 0:
            category = categories[0]["title"]

        events.append({

            "id": event["id"],

            "title": event["title"],

            "category": category,

            "latitude": coordinates[1],

            "longitude": coordinates[0],

            "date": geometry[-1]["date"]

        })

    return events