import joblib

from sklearn.ensemble import RandomForestClassifier


class ModelTrainer:

    @staticmethod
    def train(X, y):

        model = RandomForestClassifier(

            n_estimators=100,

            random_state=42

        )

        model.fit(X, y)

        joblib.dump(

            model,

            "models/disaster_risk.pkl"

        )

        return model