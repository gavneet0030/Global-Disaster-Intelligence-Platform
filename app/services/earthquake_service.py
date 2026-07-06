from sqlalchemy.orm import Session

from app.models.earthquake import Earthquake


def save_earthquakes(
    db: Session,
    earthquakes
):

    for quake in earthquakes:

        exists = db.query(Earthquake).filter(

            Earthquake.usgs_id == quake["id"]

        ).first()

        if exists:

            continue

        new = Earthquake(

            usgs_id=quake["id"],

            place=quake["place"],

            magnitude=quake["magnitude"],

            latitude=quake["latitude"],

            longitude=quake["longitude"],

            depth=quake["depth"],

            time=str(quake["time"])

        )

        db.add(new)

    db.commit()


def get_all_earthquakes(db: Session):

    return db.query(Earthquake).all()
