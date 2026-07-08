from app.ai.model_loader import ModelLoader


class Predictor:

    model = ModelLoader.load()

    @staticmethod
    def predict(data):

        prediction = Predictor.model.predict(data)

        probability = Predictor.model.predict_proba(data)

        return {

            "prediction": prediction.tolist(),

            "probability": probability.tolist()

        }