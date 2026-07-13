from app.ai.train_random_forest import RandomForestTrainer
from app.ai.train_xgboost import XGBoostTrainer
from app.ai.train_lightgbm import LightGBMTrainer
from app.ai.train_catboost import CatBoostTrainer


class ModelComparison:

    @staticmethod
    def compare():

        results = {

            "Random Forest":

                RandomForestTrainer.train(),

            "XGBoost":

                XGBoostTrainer.train(),

            "LightGBM":

                LightGBMTrainer.train(),

            "CatBoost":

                CatBoostTrainer.train()

        }

        print()

        print("=" * 60)

        print("MODEL LEADERBOARD")

        print("=" * 60)

        print()

        for model, score in sorted(

            results.items(),

            key=lambda x: x[1],

            reverse=True

        ):

            print(

                f"{model:<20} {score:.4f}"

            )

        best = max(

            results,

            key=results.get

        )

        print()

        print("=" * 60)

        print(

            "BEST MODEL :", best

        )

        print("=" * 60)

        return results