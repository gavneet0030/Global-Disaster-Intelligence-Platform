from sklearn.preprocessing import LabelEncoder


class DataPreprocessor:

    @staticmethod
    def preprocess(df):

        disaster_encoder = LabelEncoder()

        risk_encoder = LabelEncoder()

        df["disaster_type"] = (

            disaster_encoder.fit_transform(

                df["disaster_type"]

            )

        )

        y = risk_encoder.fit_transform(

            df["risk"]

        )

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

        return (

            X,

            y,

            disaster_encoder,

            risk_encoder,

        )