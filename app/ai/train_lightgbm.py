from pathlib import Path

import joblib

from sklearn.metrics import accuracy_score

from lightgbm import LGBMClassifier

from app.ai.data_loader import DatasetLoader
from app.ai.preprocessing import DataPreprocessor
from app.ai.base_trainer import BaseTrainer


class LightGBMTrainer:

    @staticmethod
    def train():

        df = DatasetLoader.load()

        X, y, _, _ = (
            DataPreprocessor.preprocess(df)
        )

        X_train, X_test, y_train, y_test = (
            BaseTrainer.split(X, y)
        )

        model = LGBMClassifier(

            n_estimators=300,

            random_state=42

        )

        model.fit(

            X_train,

            y_train

        )

        prediction = model.predict(

            X_test

        )

        accuracy = accuracy_score(

            y_test,

            prediction

        )

        base = Path(__file__).resolve().parents[2]

        models = base / "models"

        joblib.dump(

            model,

            models / "lightgbm.pkl"

        )

        print("=" * 60)

        print("LIGHTGBM")

        print("=" * 60)

        print()

        print("Accuracy :", accuracy)

        return accuracy