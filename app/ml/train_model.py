import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv(
    "dataset/disaster_dataset.csv"
)

X = df[
    [
        "temperature",
        "humidity",
        "wind_speed",
        "pressure",
        "rainfall"
    ]
]

y = df["risk"]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

joblib.dump(
    model,
    "app/ml/model.pkl"
)

print("AI Model Trained Successfully")