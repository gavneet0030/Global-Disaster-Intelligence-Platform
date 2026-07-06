from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.external_api.usgs_service import get_live_earthquakes

from app.services.sync_service import sync_earthquakes

from app.services.earthquake_service import (
    get_all_earthquakes,
    get_latest_earthquake,
    get_by_magnitude
)

from app.schemas.earthquake_filter import MagnitudeFilter


router = APIRouter(
    prefix="/earthquakes",
    tags=["Earthquakes"]
)


@router.get("/live")
def live_earthquakes():

    return get_live_earthquakes()


@router.post("/sync")
def sync_database(
    db: Session = Depends(get_db)
):

    return sync_earthquakes(db)


@router.get("/database")
def database(
    db: Session = Depends(get_db)
):

    return get_all_earthquakes(db)


@router.get("/latest")
def latest(
    db: Session = Depends(get_db)
):

    return get_latest_earthquake(db)


@router.post("/filter")
def filter_magnitude(
    request: MagnitudeFilter,
    db: Session = Depends(get_db)
):

    return get_by_magnitude(
        db,
        request.minimum
    )