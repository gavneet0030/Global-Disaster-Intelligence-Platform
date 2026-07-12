from app.ai.risk_score import RiskScore


class FeatureEngineering:

    @staticmethod
    def transform(events):

        engineered = []

        for event in events:

            score = RiskScore.calculate(event)

            engineered.append({

                "title": event["title"],

                "latitude": event["latitude"],

                "longitude": event["longitude"],

                "source": event["source"],

                "risk_score": score,

                "severity": RiskScore.severity(score),

                "confidence": RiskScore.confidence(score)

            })

        return engineered