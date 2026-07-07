from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.external_api.nasa_service import get_nasa_events

from app.services.nasa_service import (
    save_events,
    get_events
)

router = APIRouter(

    prefix="/nasa",

    tags=["NASA Events"]

)


@router.get("/live")
def live_events():

    return get_nasa_events()


@router.post("/sync")
def sync_events(
    db: Session = Depends(get_db)
):

    events = get_nasa_events()

    inserted = save_events(
        db,
        events
    )

    return {

        "inserted": inserted,

        "total": len(events)

    }


@router.get("/database")
def database_events(
    db: Session = Depends(get_db)
):

    return get_events(db)