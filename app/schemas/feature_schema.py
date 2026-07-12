from pydantic import BaseModel


class EngineeredEvent(BaseModel):

    title: str

    latitude: float

    longitude: float

    source: str

    risk_score: float

    severity: str

    confidence: float