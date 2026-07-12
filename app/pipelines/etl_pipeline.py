from app.ingestion.disaster_ingestion import DisasterIngestion
from app.validators.event_validator import EventValidator
from app.utils.duplicate_checker import DuplicateChecker


class ETLPipeline:

    @staticmethod
    def run():

        # Fetch data from APIs
        data = DisasterIngestion.fetch_all()

        nasa_events = []
        earthquake_events = []

        # -----------------------------
        # Validate NASA Events
        # -----------------------------
        for event in data.get("nasa", []):

            if EventValidator.validate(event):
                nasa_events.append(event)

        # -----------------------------
        # Validate Earthquake Events
        # -----------------------------
        for event in data.get("earthquakes", []):

            if EventValidator.validate(event):
                earthquake_events.append(event)

        # -----------------------------
        # Merge all events
        # -----------------------------
        all_events = nasa_events + earthquake_events

        # -----------------------------
        # Remove duplicates
        # -----------------------------
        unique_events = DuplicateChecker.remove_duplicates(
            all_events
        )

        # -----------------------------
        # Return
        # -----------------------------
        return {

            "nasa": nasa_events,

            "earthquakes": earthquake_events,

            "unique_events": unique_events

        }