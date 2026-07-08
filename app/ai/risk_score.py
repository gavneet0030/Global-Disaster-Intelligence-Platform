class RiskScore:

    @staticmethod
    def calculate(probability):

        probability = probability * 100

        if probability >= 80:
            return "Extreme"

        elif probability >= 60:
            return "High"

        elif probability >= 40:
            return "Medium"

        return "Low"