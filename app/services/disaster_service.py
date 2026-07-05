from sqlalchemy.orm import Session

from app.models.disaster import Disaster
from app.schemas.disaster import (
    DisasterCreate,
    DisasterUpdate
)


def create_disaster(
    db: Session,
    disaster: DisasterCreate
):

    db_disaster = Disaster(
        disaster_type=disaster.disaster_type,
        country=disaster.country,
        state=disaster.state,
        city=disaster.city,
        latitude=disaster.latitude,
        longitude=disaster.longitude,
        severity=disaster.severity,
        status=disaster.status,
        description=disaster.description,
        source=disaster.source
    )

    db.add(db_disaster)
    db.commit()
    db.refresh(db_disaster)

    return db_disaster


def get_all_disasters(
    db: Session,
    disaster_type: str = None
):

    query = db.query(Disaster)

    if disaster_type:
        query = query.filter(
            Disaster.disaster_type == disaster_type
        )

    return query.all()


def get_disaster_by_id(
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


def update_disaster(
    db: Session,
    disaster_id: int,
    disaster: DisasterUpdate
):

    db_disaster = (
        db.query(Disaster)
        .filter(
            Disaster.id == disaster_id
        )
        .first()
    )

    if db_disaster is None:
        return None

    db_disaster.disaster_type = disaster.disaster_type
    db_disaster.country = disaster.country
    db_disaster.state = disaster.state
    db_disaster.city = disaster.city
    db_disaster.latitude = disaster.latitude
    db_disaster.longitude = disaster.longitude
    db_disaster.severity = disaster.severity
    db_disaster.status = disaster.status
    db_disaster.description = disaster.description
    db_disaster.source = disaster.source

    db.commit()
    db.refresh(db_disaster)

    return db_disaster


def delete_disaster(
    db: Session,
    disaster_id: int
):

    db_disaster = (
        db.query(Disaster)
        .filter(
            Disaster.id == disaster_id
        )
        .first()
    )

    if db_disaster is None:
        return None

    db.delete(db_disaster)
    db.commit()

    return db_disaster