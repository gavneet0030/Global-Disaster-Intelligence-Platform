from app.ingestion.disaster_ingestion import DisasterIngestion

from app.agents.base_agent import BaseAgent


class MonitoringAgent(BaseAgent):

    def run(self, data=None):

        disasters = DisasterIngestion.fetch_all()

        return disasters