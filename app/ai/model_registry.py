from pathlib import Path

import joblib


class ModelRegistry:

    @staticmethod
    def save(

        model,

        filename

    ):

        base = Path(__file__).resolve().parents[2]

        models = base / "models"

        models.mkdir(exist_ok=True)

        path = models / filename

        joblib.dump(

            model,

            path

        )

        return path

    @staticmethod
    def load(

        filename

    ):

        base = Path(__file__).resolve().parents[2]

        path = (

            base

            / "models"

            / filename

        )

        return joblib.load(path)