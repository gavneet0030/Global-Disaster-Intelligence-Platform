from pathlib import Path

import joblib

from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier

from app.ai.data_loader import DatasetLoader
from app.ai.preprocessing import DataPreprocessor
from app.ai.base_trainer import BaseTrainer


class XGBoostTrainer:

    @staticmethod
    def train():

        df = DatasetLoader.load()

        X, y, _, _ = (
            DataPreprocessor.preprocess(df)
        )

        X_train, X_test, y_train, y_test = (
            BaseTrainer.split(X, y)
        )

        model = XGBClassifier(

            n_estimators=300,

            learning_rate=0.05,

            max_depth=8,

            random_state=42,

            eval_metric="mlogloss"

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

            models / "xgboost.pkl"

        )

        print("=" * 60)

        print("XGBOOST")

        print("=" * 60)

        print()

        print("Accuracy :", accuracy)

        return accuracy