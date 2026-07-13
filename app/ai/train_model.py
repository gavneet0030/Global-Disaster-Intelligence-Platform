from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


class ModelTrainer:

    @staticmethod
    def train():

        # -------------------------------------------------
        # Project Paths
        # -------------------------------------------------

        BASE_DIR = Path(__file__).resolve().parents[2]

        DATASET_PATH = BASE_DIR / "dataset" / "disaster_training.csv"

        MODEL_DIR = BASE_DIR / "models"

        MODEL_DIR.mkdir(exist_ok=True)

        # -------------------------------------------------
        # Check Dataset
        # -------------------------------------------------

        if not DATASET_PATH.exists():

            raise FileNotFoundError(

                f"\nDataset not found:\n{DATASET_PATH}"

            )

        # -------------------------------------------------
        # Load Dataset
        # -------------------------------------------------

        df = pd.read_csv(DATASET_PATH)

        print("=" * 60)
        print("DATASET LOADED")
        print("=" * 60)

        print("\nShape :", df.shape)

        print("\nColumns :")

        print(df.columns.tolist())

        print("\nFirst Five Rows")

        print(df.head())

        # -------------------------------------------------
        # Encode Disaster Type
        # -------------------------------------------------

        disaster_encoder = LabelEncoder()

        df["disaster_type"] = disaster_encoder.fit_transform(

            df["disaster_type"]

        )

        # -------------------------------------------------
        # Encode Target
        # -------------------------------------------------

        risk_encoder = LabelEncoder()

        y = risk_encoder.fit_transform(

            df["risk"]

        )

        # -------------------------------------------------
        # Features
        # -------------------------------------------------

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

        # -------------------------------------------------
        # Train Test Split
        # -------------------------------------------------

        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=42,

            stratify=y

        )

        print("\nTraining Samples :", len(X_train))

        print("Testing Samples  :", len(X_test))

        # -------------------------------------------------
        # Model
        # -------------------------------------------------

        model = RandomForestClassifier(

            n_estimators=300,

            max_depth=15,

            random_state=42,

            n_jobs=-1

        )

        print("\nTraining Model...\n")

        model.fit(

            X_train,

            y_train

        )

        # -------------------------------------------------
        # Prediction
        # -------------------------------------------------

        predictions = model.predict(

            X_test

        )

        # -------------------------------------------------
        # Evaluation
        # -------------------------------------------------

        accuracy = accuracy_score(

            y_test,

            predictions

        )

        print("=" * 60)

        print("MODEL ACCURACY")

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

        # -------------------------------------------------
        # Save Files
        # -------------------------------------------------

        MODEL_PATH = MODEL_DIR / "disaster_risk.pkl"

        DISASTER_ENCODER_PATH = MODEL_DIR / "disaster_encoder.pkl"

        RISK_ENCODER_PATH = MODEL_DIR / "risk_encoder.pkl"

        joblib.dump(

            model,

            MODEL_PATH

        )

        joblib.dump(

            disaster_encoder,

            DISASTER_ENCODER_PATH

        )

        joblib.dump(

            risk_encoder,

            RISK_ENCODER_PATH

        )

        print("\nModel Saved Successfully")

        print(MODEL_PATH)

        return model