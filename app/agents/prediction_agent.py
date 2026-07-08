from app.agents.base_agent import BaseAgent


class PredictionAgent(BaseAgent):

    def run(self, disasters):

        return {

            "status": "Prediction Engine Ready",

            "events": disasters

        }