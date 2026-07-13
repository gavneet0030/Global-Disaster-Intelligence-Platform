from pathlib import Path

import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from sklearn.model_selection import train_test_split


class ModelEvaluator:

    @staticmethod
    def evaluate():

        BASE_DIR = Path(__file__).resolve().parents[2]

        dataset_path = BASE_DIR / "dataset" / "disaster_training.csv"

        model_path = BASE_DIR / "models" / "disaster_risk.pkl"

        disaster_encoder = joblib.load(
            BASE_DIR / "models" / "disaster_encoder.pkl"
        )

        risk_encoder = joblib.load(
            BASE_DIR / "models" / "risk_encoder.pkl"
        )

        model = joblib.load(model_path)

        df = pd.read_csv(dataset_path)

        df["disaster_type"] = disaster_encoder.transform(
            df["disaster_type"]
        )

        y = risk_encoder.transform(
            df["risk"]
        )

        X = df[
            [
                "temperature",
                "humidity",
                "wind_speed",
                "pressure",
                "rainfall",
                "disaster_type"
            ]
        ]

        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=42,

            stratify=y

        )

        predictions = model.predict(X_test)

        print("=" * 60)

        print("MODEL EVALUATION")

        print("=" * 60)

        print()

        print("Accuracy")

        print(
            accuracy_score(
                y_test,
                predictions
            )
        )

        print()

        print("Precision")

        print(
            precision_score(
                y_test,
                predictions,
                average="weighted"
            )
        )

        print()

        print("Recall")

        print(
            recall_score(
                y_test,
                predictions,
                average="weighted"
            )
        )

        print()

        print("F1 Score")

        print(
            f1_score(
                y_test,
                predictions,
                average="weighted"
            )
        )

        print()

        print("Classification Report")

        print(
            classification_report(
                y_test,
                predictions
            )
        )

        cm = confusion_matrix(
            y_test,
            predictions
        )

        print()

        print("Confusion Matrix")

        print(cm)

        plt.figure(figsize=(8, 6))

        plt.imshow(cm)

        plt.title("Confusion Matrix")

        plt.colorbar()

        plt.xlabel("Predicted")

        plt.ylabel("Actual")

        plt.tight_layout()

        plt.show()

        print()

        print("Feature Importance")

        print()

        for feature, score in zip(

            X.columns,

            model.feature_importances_

        ):

            print(

                f"{feature:<20}{score:.4f}"

            )