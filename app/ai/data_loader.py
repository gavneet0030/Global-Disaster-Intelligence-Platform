from pathlib import Path

import pandas as pd


class DatasetLoader:

    @staticmethod
    def load():

        base_dir = Path(__file__).resolve().parents[2]

        dataset = (
            base_dir
            / "dataset"
            / "disaster_training.csv"
        )

        if not dataset.exists():

            raise FileNotFoundError(

                f"Dataset not found\n{dataset}"

            )

        df = pd.read_csv(dataset)

        print("=" * 60)

        print("DATASET LOADED")

        print("=" * 60)

        print()

        print("Rows :", len(df))

        print("Columns :", len(df.columns))

        print()

        return df