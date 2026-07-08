import pandas as pd


class DataPreprocessing:

    @staticmethod
    def clean(df):

        df = df.drop_duplicates()

        df = df.dropna()

        return df