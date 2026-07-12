from typing import Dict, Any


class WeatherValidator:

    @staticmethod
    def validate(weather: Dict[str, Any]) -> bool:

        required = [

            "temperature",

            "humidity",

            "city"

        ]

        for field in required:

            if field not in weather:
                return False

            if weather[field] is None:
                return False

        return True