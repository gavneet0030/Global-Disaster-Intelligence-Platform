from app.ai.train_random_forest import RandomForestTrainer

from app.ai.train_xgboost import XGBoostTrainer

from app.ai.train_lightgbm import LightGBMTrainer


def main():

    print()

    rf = RandomForestTrainer.train()

    print()

    xgb = XGBoostTrainer.train()

    print()

    lgb = LightGBMTrainer.train()

    print()

    print("=" * 60)

    print("SUMMARY")

    print("=" * 60)

    print()

    print("Random Forest :", rf)

    print("XGBoost       :", xgb)

    print("LightGBM      :", lgb)


if __name__ == "__main__":

    main()