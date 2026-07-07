from fastapi import APIRouter

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse
)

from app.ml.predict import predict_risk

router = APIRouter(
    prefix="/prediction",
    tags=["AI Prediction"]
)


@router.post(
    "/risk",
    response_model=PredictionResponse
)
def predict(
    request: PredictionRequest
):

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