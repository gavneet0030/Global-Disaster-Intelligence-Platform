class RiskScore:
    
    @staticmethod
    def calculate(event):

        score = 0

        title = event.get("title", "").lower()

        if "wildfire" in title:
            score += 80

        elif "earthquake" in title:
            score += 90

        elif "flood" in title:
            score += 70

        else:
            score += 40

        return min(score, 100)

    @staticmethod
    def severity(score):

        if score >= 85:
            return "Critical"

        if score >= 70:
            return "High"

        if score >= 50:
            return "Medium"

        return "Low"

    @staticmethod
    def confidence(score):

        return round(score / 100, 2)