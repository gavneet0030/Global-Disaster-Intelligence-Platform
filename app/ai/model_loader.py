import joblib


class ModelLoader:

    @staticmethod
    def load():

        return joblib.load(

            "models/disaster_risk.pkl"

        )