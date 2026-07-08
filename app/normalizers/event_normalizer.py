from datetime import datetime


class EventNormalizer:

    @staticmethod
    def normalize_nasa(event):

        geometry = event["geometry"][-1]

        return {

            "event_id": event["id"],

            "title": event["title"],

            "category": event["categories"][0]["title"],

            "latitude": geometry["coordinates"][1],

            "longitude": geometry["coordinates"][0],

            "date": datetime.fromisoformat(
                geometry["date"].replace("Z", "")
            )

        }

    @staticmethod
    def normalize_earthquake(feature):

        coordinates = feature["geometry"]["coordinates"]

        return {

            "event_id": feature["id"],

            "title": feature["properties"]["title"],

            "magnitude": feature["properties"]["mag"],

            "latitude": coordinates[1],

            "longitude": coordinates[0],

            "depth": coordinates[2]

        }