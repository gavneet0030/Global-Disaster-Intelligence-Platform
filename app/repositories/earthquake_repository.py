from sqlalchemy.orm import Session

from app.models.earthquake import Earthquake


class EarthquakeRepository:

    @staticmethod
    def create(
        db: Session,
        earthquake: Earthquake
    ):

        db.add(earthquake)
        db.commit()
        db.refresh(earthquake)

        return earthquake

    @staticmethod
    def get_all(
        db: Session
    ):

        return (
            db.query(Earthquake)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        earthquake_id: int
    ):

        return (
            db.query(Earthquake)
            .filter(
                Earthquake.id == earthquake_id
            )
            .first()
        )

    @staticmethod
    def get_recent(
        db: Session,
        limit: int = 20
    ):

        return (
            db.query(Earthquake)
            .order_by(
                Earthquake.id.desc()
            )
            .limit(limit)
            .all()
        )

    @staticmethod
    def delete(
        db: Session,
        earthquake_id: int
    ):

        earthquake = (
            db.query(Earthquake)
            .filter(
                Earthquake.id == earthquake_id
            )
            .first()
        )

        if earthquake:

            db.delete(earthquake)
            db.commit()

        return earthquake