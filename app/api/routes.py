from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.disaster import (
    DisasterCreate,
    DisasterUpdate,
    DisasterResponse
)
from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse
)

from app.services.user_service import create_user
from app.services.auth_service import login_user
from app.services.disaster_service import (
    create_disaster,
    get_all_disasters,
    get_disaster_by_id,
    update_disaster,
    delete_disaster
)

from app.services.weather_service import get_weather
from app.ml.predict import predict_risk

router = APIRouter()


# ---------------- HOME ---------------- #

@router.get("/")
def home():
    return {
        "message": "Welcome to Global Disaster Intelligence Platform V2.0"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ---------------- USER ---------------- #

@router.post("/users", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)


# ---------------- LOGIN ---------------- #

@router.post("/login", response_model=TokenResponse)
def login(
    login: LoginRequest,
    db: Session = Depends(get_db)
):

    token = login_user(db, login)

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return token


# ---------------- DISASTER CRUD ---------------- #

@router.post(
    "/disasters",
    response_model=DisasterResponse
)
def add_disaster(
    disaster: DisasterCreate,
    db: Session = Depends(get_db)
):
    return create_disaster(db, disaster)


@router.get(
    "/disasters",
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
    "/disasters/{disaster_id}",
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
    "/disasters/{disaster_id}",
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


@router.delete("/disasters/{disaster_id}")
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


# ---------------- WEATHER ---------------- #

@router.get("/weather/{city}")
def weather(city: str):

    data = get_weather(city)

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    return data


# ---------------- AI PREDICTION ---------------- #

@router.post(
    "/predict-risk",
    response_model=PredictionResponse
)
def predict(request: PredictionRequest):

    risk = predict_risk(
        request.temperature,
        request.humidity,
        request.wind_speed,
        request.pressure,
        request.rainfall
    )

    return {
        "risk": risk
    }