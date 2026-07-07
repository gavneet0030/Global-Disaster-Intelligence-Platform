from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.disaster import (
    DisasterCreate,
    DisasterUpdate,
    DisasterResponse
)

from app.services.disaster_service import (
    create_disaster,
    get_all_disasters,
    get_disaster_by_id,
    update_disaster,
    delete_disaster
)

router = APIRouter(
    prefix="/disasters",
    tags=["Disasters"]
)


@router.post(
    "",
    response_model=DisasterResponse
)
def add_disaster(
    disaster: DisasterCreate,
    db: Session = Depends(get_db)
):

    return create_disaster(
        db,
        disaster
    )


@router.get(
    "",
    response_model=list[DisasterResponse]
)
def get_disasters(
    disaster_type: str = None,
    db: Session = Depends(get_db)
):

    return get_all_disasters(
        db,
        disaster_type
    )


@router.get(
    "/{disaster_id}",
    response_model=DisasterResponse
)
def get_disaster(
    disaster_id: int,
    db: Session = Depends(get_db)
):

    disaster = get_disaster_by_id(
        db,
        disaster_id
    )

    if disaster is None:

        raise HTTPException(
            status_code=404,
            detail="Disaster not found"
        )

    return disaster


@router.put(
    "/{disaster_id}",
    response_model=DisasterResponse
)
def edit_disaster(
    disaster_id: int,
    disaster: DisasterUpdate,
    db: Session = Depends(get_db)
):

    updated = update_disaster(
        db,
        disaster_id,
        disaster
    )

    if updated is None:

        raise HTTPException(
            status_code=404,
            detail="Disaster not found"
        )

    return updated


@router.delete("/{disaster_id}")
def remove_disaster(
    disaster_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_disaster(
        db,
        disaster_id
    )

    if deleted is None:

        raise HTTPException(
            status_code=404,
            detail="Disaster not found"
        )

    return {
        "message": "Disaster deleted successfully"
    }