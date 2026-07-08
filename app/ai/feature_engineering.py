import pandas as pd


class FeatureEngineering:

    @staticmethod
    def prepare(df: pd.DataFrame):

        features = df[

            [
                "latitude",
                "longitude",
                "magnitude",
                "depth"
            ]

        ]

        return features