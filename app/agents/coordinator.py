from app.agents.monitoring_agent import MonitoringAgent

from app.agents.prediction_agent import PredictionAgent

from app.agents.alert_agent import AlertAgent


class Coordinator:

    def __init__(self):

        self.monitor = MonitoringAgent()

        self.predict = PredictionAgent()

        self.alert = AlertAgent()

    def execute(self):

        disasters = self.monitor.run()

        prediction = self.predict.run(
            disasters
        )

        alerts = self.alert.run(
            prediction
        )

        return alerts