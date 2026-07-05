from pydantic import BaseModel


class PredictionRequest(BaseModel):

    temperature: float

    humidity: float

    wind_speed: float

    pressure: float

    rainfall: float


class PredictionResponse(BaseModel):

    risk: str