from pathlib import Path

import joblib

from catboost import CatBoostClassifier

from sklearn.metrics import accuracy_score

from app.ai.data_loader import DatasetLoader
from app.ai.preprocessing import DataPreprocessor
from app.ai.base_trainer import BaseTrainer


class CatBoostTrainer:

    @staticmethod
    def train():

        df = DatasetLoader.load()

        X, y, _, _ = (

            DataPreprocessor.preprocess(df)

        )

        X_train, X_test, y_train, y_test = (

            BaseTrainer.split(

                X,

                y

            )

        )

        model = CatBoostClassifier(

            iterations=300,

            learning_rate=0.05,

            depth=8,

            verbose=False,

            random_seed=42

        )

        print("=" * 60)

        print("CATBOOST TRAINING")

        print("=" * 60)

        print()

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

        models.mkdir(exist_ok=True)

        joblib.dump(

            model,

            models / "catboost.pkl"

        )

        print()

        print("Accuracy :", accuracy)

        print()

        print("Model Saved Successfully")

        return accuracy