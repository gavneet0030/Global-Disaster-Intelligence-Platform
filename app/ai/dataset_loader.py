import pandas as pd


class DatasetLoader:

    @staticmethod
    def load_csv(path):

        return pd.read_csv(path)