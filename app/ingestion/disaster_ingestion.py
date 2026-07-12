from app.external_api.nasa_service import fetch_nasa_events
from app.external_api.usgs_service import fetch_earthquakes

from app.normalizers.event_normalizer import EventNormalizer


class DisasterIngestion:

    @staticmethod
    def fetch_all():

        # Fetch raw data
        nasa = fetch_nasa_events()
        earthquakes = fetch_earthquakes()

        # Normalized data
        nasa_events = []

        for event in nasa:

            normalized = EventNormalizer.normalize_nasa(event)

            if normalized is not None:
                nasa_events.append(normalized)

        earthquake_events = []

        for event in earthquakes:

            normalized = EventNormalizer.normalize_earthquake(event)

            if normalized is not None:
                earthquake_events.append(normalized)

        return {

            "nasa": nasa_events,

            "earthquakes": earthquake_events

        }