from sqlalchemy.orm import Session

from app.ingestion.disaster_ingestion import DisasterIngestion


class IngestionService:

    @staticmethod
    def fetch():

        return DisasterIngestion.fetch_all()