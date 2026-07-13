from pathlib import Path

import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from app.ai.data_loader import DatasetLoader
from app.ai.preprocessing import DataPreprocessor
from app.ai.base_trainer import BaseTrainer


class RandomForestTrainer:

    @staticmethod
    def train():

        df = DatasetLoader.load()

        X, y, disaster_encoder, risk_encoder = (
            DataPreprocessor.preprocess(df)
        )

        X_train, X_test, y_train, y_test = (
            BaseTrainer.split(X, y)
        )

        model = RandomForestClassifier(

            n_estimators=200,

            random_state=42

        )

        model.fit(

            X_train,

            y_train

        )

        predictions = model.predict(

            X_test

        )

        accuracy = accuracy_score(

            y_test,

            predictions

        )

        base = Path(__file__).resolve().parents[2]

        models = base / "models"

        models.mkdir(exist_ok=True)

        joblib.dump(

            model,

            models / "random_forest.pkl"

        )

        joblib.dump(

            disaster_encoder,

            models / "disaster_encoder.pkl"

        )

        joblib.dump(

            risk_encoder,

            models / "risk_encoder.pkl"

        )

        print("=" * 60)

        print("RANDOM FOREST")

        print("=" * 60)

        print()

        print("Accuracy :", accuracy)

        return accuracy