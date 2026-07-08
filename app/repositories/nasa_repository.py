from sqlalchemy.orm import Session

from app.models.nasa_event import NASAEvent


class NASARepository:

    @staticmethod
    def create(
        db: Session,
        event: NASAEvent
    ):

        db.add(event)
        db.commit()
        db.refresh(event)

        return event

    @staticmethod
    def get_all(
        db: Session
    ):

        return (
            db.query(NASAEvent)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        event_id: int
    ):

        return (
            db.query(NASAEvent)
            .filter(
                NASAEvent.id == event_id
            )
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        event_id: int
    ):

        event = (
            db.query(NASAEvent)
            .filter(
                NASAEvent.id == event_id
            )
            .first()
        )

        if event:

            db.delete(event)
            db.commit()

        return event