from fastapi import APIRouter

from app.ai.predict_model import DisasterPredictor
from app.schemas.prediction_request import PredictionRequest

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)

predictor = DisasterPredictor()


@router.post("/risk")
def predict_risk(request: PredictionRequest):

    return predictor.predict(

        temperature=request.temperature,

        humidity=request.humidity,

        wind_speed=request.wind_speed,

        pressure=request.pressure,

        rainfall=request.rainfall,

        disaster_type=request.disaster_type

    )