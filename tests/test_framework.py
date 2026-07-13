from app.ai.data_loader import DatasetLoader

from app.ai.preprocessing import DataPreprocessor

from app.ai.base_trainer import BaseTrainer


def main():

    df = DatasetLoader.load()

    X, y, _, _ = (

        DataPreprocessor.preprocess(

            df

        )

    )

    X_train, X_test, y_train, y_test = (

        BaseTrainer.split(

            X,

            y

        )

    )

    print("=" * 60)

    print("FRAMEWORK TEST")

    print("=" * 60)

    print()

    print("Training :", len(X_train))

    print("Testing  :", len(X_test))


if __name__ == "__main__":

    main()