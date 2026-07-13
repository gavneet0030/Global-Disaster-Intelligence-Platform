from pathlib import Path

import joblib
import pandas as pd


class DisasterPredictor:

    def __init__(self):

        BASE_DIR = Path(__file__).resolve().parents[2]

        MODEL_DIR = BASE_DIR / "models"

        self.model = joblib.load(
            MODEL_DIR / "disaster_risk.pkl"
        )

        self.disaster_encoder = joblib.load(
            MODEL_DIR / "disaster_encoder.pkl"
        )

        self.risk_encoder = joblib.load(
            MODEL_DIR / "risk_encoder.pkl"
        )

    def predict(

        self,

        temperature,

        humidity,

        wind_speed,

        pressure,

        rainfall,

        disaster_type

    ):

        disaster_type = self.disaster_encoder.transform(
            [disaster_type]
        )[0]

        sample = pd.DataFrame(
            [
                {
                    "temperature": temperature,
                    "humidity": humidity,
                    "wind_speed": wind_speed,
                    "pressure": pressure,
                    "rainfall": rainfall,
                    "disaster_type": disaster_type,
                }
            ]
        )

        prediction = self.model.predict(sample)[0]

        probability = self.model.predict_proba(sample).max()

        risk = self.risk_encoder.inverse_transform(
            [prediction]
        )[0]

        return {

            "risk": risk,

            "confidence": round(

                float(probability),

                4

            )

        }