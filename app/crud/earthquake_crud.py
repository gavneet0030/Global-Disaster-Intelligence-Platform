from sqlalchemy.orm import Session

from app.models.earthquake import Earthquake


def earthquake_exists(
    db: Session,
    usgs_id: str
):

    return (

        db.query(Earthquake)

        .filter(

            Earthquake.usgs_id == usgs_id

        )

        .first()

    )


def create_earthquake(

    db: Session,

    data

):

    earthquake = Earthquake(

        usgs_id=data["id"],

        place=data["place"],

        magnitude=data["magnitude"],

        latitude=data["latitude"],

        longitude=data["longitude"],

        depth=data["depth"],

        time=str(data["time"])

    )

    db.add(earthquake)

    db.commit()

    db.refresh(earthquake)

    return earthquake


def get_all_earthquakes(

    db: Session

):

    return (

        db.query(Earthquake)

        .order_by(

            Earthquake.id.desc()

        )

        .all()

    )