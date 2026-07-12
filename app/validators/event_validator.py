from typing import Dict, Any


class EventValidator:

    REQUIRED_FIELDS = [
        "title",
        "latitude",
        "longitude",
        "source"
    ]

    @staticmethod
    def validate(event: Dict[str, Any]) -> bool:

        # Check required fields

        for field in EventValidator.REQUIRED_FIELDS:

            if field not in event:
                return False

            if event[field] is None:
                return False

            if str(event[field]).strip() == "":
                return False

        # Validate latitude

        latitude = event["latitude"]

        if not isinstance(latitude, (int, float)):
            return False

        if latitude < -90 or latitude > 90:
            return False

        # Validate longitude

        longitude = event["longitude"]

        if not isinstance(longitude, (int, float)):
            return False

        if longitude < -180 or longitude > 180:
            return False

        return True