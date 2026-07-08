from app.agents.base_agent import BaseAgent


class AlertAgent(BaseAgent):

    def run(self, prediction):

        return {

            "alert": True,

            "prediction": prediction

        }