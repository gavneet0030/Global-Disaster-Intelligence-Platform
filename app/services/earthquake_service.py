from sqlalchemy.orm import Session

from app.models.earthquake import Earthquake


def get_all_earthquakes(db: Session):

    return (

        db.query(Earthquake)

        .order_by(Earthquake.id.desc())

        .all()

    )


def get_latest_earthquake(db: Session):

    return (

        db.query(Earthquake)

        .order_by(Earthquake.id.desc())

        .first()

    )


def get_by_magnitude(

    db: Session,

    minimum: float

):

    return (

        db.query(Earthquake)

        .filter(

            Earthquake.magnitude >= minimum

        )

        .all()

    )