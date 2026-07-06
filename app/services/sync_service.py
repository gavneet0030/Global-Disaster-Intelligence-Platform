from sqlalchemy.orm import Session

from app.external_api.usgs_service import get_live_earthquakes

from app.crud.earthquake_crud import (

    earthquake_exists,

    create_earthquake

)


def sync_earthquakes(

    db: Session

):

    earthquakes = get_live_earthquakes()

    count = 0

    for quake in earthquakes:

        exists = earthquake_exists(

            db,

            quake["id"]

        )

        if exists:

            continue

        create_earthquake(

            db,

            quake

        )

        count += 1

    return {

        "inserted": count,

        "total": len(earthquakes)

    }