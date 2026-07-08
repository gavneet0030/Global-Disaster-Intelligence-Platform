from app.external_api.nasa_service import (
    fetch_nasa_events
)

from app.external_api.earthquake_service import (
    fetch_earthquakes
)

from app.normalizers.event_normalizer import (
    EventNormalizer
)


class DisasterIngestion:

    @staticmethod
    def fetch_all():

        nasa = fetch_nasa_events()

        earthquakes = fetch_earthquakes()

        nasa_events = [

            EventNormalizer.normalize_nasa(x)

            for x in nasa

        ]

        earthquake_events = [

            EventNormalizer.normalize_earthquake(x)

            for x in earthquakes

        ]

        return {

            "nasa": nasa_events,

            "earthquakes": earthquake_events

        }