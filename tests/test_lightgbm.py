from pathlib import Path

import joblib
import pandas as pd

from lightgbm import LGBMClassifier

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


class LightGBMTrainer:

    @staticmethod
    def train():

        BASE_DIR = Path(__file__).resolve().parents[2]

        DATASET_PATH = BASE_DIR / "dataset" / "disaster_training.csv"

        MODEL_DIR = BASE_DIR / "models"

        MODEL_DIR.mkdir(exist_ok=True)

        print("=" * 60)
        print("LIGHTGBM TRAINING")
        print("=" * 60)

        if not DATASET_PATH.exists():

            raise FileNotFoundError(
                f"Dataset not found:\n{DATASET_PATH}"
            )

        df = pd.read_csv(DATASET_PATH)

        disaster_encoder = LabelEncoder()

        df["disaster_type"] = disaster_encoder.fit_transform(
            df["disaster_type"]
        )

        risk_encoder = LabelEncoder()

        y = risk_encoder.fit_transform(
            df["risk"]
        )

        X = df[
            [
                "temperature",
                "humidity",
                "wind_speed",
                "pressure",
                "rainfall",
                "disaster_type",
            ]
        ]

        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=42,

            stratify=y

        )

        model = LGBMClassifier(

            n_estimators=300,

            learning_rate=0.05,

            max_depth=8,

            random_state=42

        )

        print("\nTraining Model...\n")

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

        print("=" * 60)

        print("RESULTS")

        print("=" * 60)

        print(f"\nAccuracy : {accuracy:.4f}")

        print("\nClassification Report\n")

        print(

            classification_report(

                y_test,

                predictions

            )

        )

        print("\nConfusion Matrix\n")

        print(

            confusion_matrix(

                y_test,

                predictions

            )

        )

        joblib.dump(

            model,

            MODEL_DIR / "lightgbm_model.pkl"

        )

        print("\nModel Saved Successfully")

        print(MODEL_DIR / "lightgbm_model.pkl")

        return model