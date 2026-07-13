from app.ai.predict_model import DisasterPredictor


def main():

    predictor = DisasterPredictor()

    result = predictor.predict(

        temperature=39,

        humidity=90,

        wind_speed=18,

        pressure=1005,

        rainfall=320,

        disaster_type="Flood"

    )

    print("=" * 50)

    print(result)

    print("=" * 50)


if __name__ == "__main__":

    main()