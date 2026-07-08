from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


class Evaluator:

    @staticmethod
    def evaluate(model, X_test, y_test):

        prediction = model.predict(X_test)

        print(

            classification_report(
                y_test,
                prediction
            )

        )

        print(

            accuracy_score(
                y_test,
                prediction
            )

        )