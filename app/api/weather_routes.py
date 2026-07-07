from fastapi import APIRouter, HTTPException

from app.services.weather_service import get_weather

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


@router.get("/{city}")
def weather(city: str):

    data = get_weather(city)

    if data is None:

        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    return data