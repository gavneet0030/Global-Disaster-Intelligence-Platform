from typing import Dict, Any


class EarthquakeValidator:

    @staticmethod
    def validate(event: Dict[str, Any]) -> bool:

        required = [

            "magnitude",

            "latitude",

            "longitude"

        ]

        for field in required:

            if field not in event:
                return False

            if event[field] is None:
                return False

        magnitude = event["magnitude"]

        if magnitude < 0:

            return False

        return True