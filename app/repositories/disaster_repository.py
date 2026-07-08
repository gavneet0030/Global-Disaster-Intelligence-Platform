from sqlalchemy.orm import Session

from app.models.disaster import Disaster


class DisasterRepository:

    @staticmethod
    def create(
        db: Session,
        disaster: Disaster
    ):

        db.add(disaster)
        db.commit()
        db.refresh(disaster)

        return disaster

    @staticmethod
    def get_all(
        db: Session
    ):

        return (
            db.query(Disaster)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        disaster_id: int
    ):

        return (
            db.query(Disaster)
            .filter(
                Disaster.id == disaster_id
            )
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        disaster_id: int
    ):

        disaster = (
            db.query(Disaster)
            .filter(
                Disaster.id == disaster_id
            )
            .first()
        )

        if disaster:

            db.delete(disaster)
            db.commit()

        return disaster

    @staticmethod
    def update(
        db: Session,
        disaster_id: int,
        updated_data: dict
    ):

        disaster = (
            db.query(Disaster)
            .filter(
                Disaster.id == disaster_id
            )
            .first()
        )

        if disaster is None:
            return None

        for key, value in updated_data.items():
            setattr(
                disaster,
                key,
                value
            )

        db.commit()
        db.refresh(disaster)

        return disaster