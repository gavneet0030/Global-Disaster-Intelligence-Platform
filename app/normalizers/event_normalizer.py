class EventNormalizer:
    
    @staticmethod
    def normalize_nasa(event):

        geometry = event.get("geometry", [])

        if not geometry:
            return None

        latest = geometry[-1]

        coordinates = latest.get("coordinates", [])

        if len(coordinates) < 2:
            return None

        return {
            "title": event.get("title", "Unknown Event"),
            "latitude": coordinates[1],
            "longitude": coordinates[0],
            "source": "NASA"
        }

    @staticmethod
    def normalize_earthquake(event):

        geometry = event.get("geometry", {})
        properties = event.get("properties", {})

        coordinates = geometry.get("coordinates", [])

        if len(coordinates) < 2:
            return None

        return {
            "title": properties.get("title", "Earthquake"),
            "latitude": coordinates[1],
            "longitude": coordinates[0],
            "magnitude": properties.get("mag", 0.0),
            "place": properties.get("place", "Unknown"),
            "time": properties.get("time"),
            "source": "USGS"
        }