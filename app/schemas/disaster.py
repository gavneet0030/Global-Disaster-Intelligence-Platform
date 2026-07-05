from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DisasterCreate(BaseModel):
    disaster_type: str
    country: str
    state: str
    city: str
    latitude: float
    longitude: float
    severity: str
    status: str
    description: Optional[str] = None
    source: str


class DisasterUpdate(BaseModel):
    disaster_type: str
    country: str
    state: str
    city: str
    latitude: float
    longitude: float
    severity: str
    status: str
    description: Optional[str] = None
    source: str


class DisasterResponse(BaseModel):
    id: int
    disaster_type: str
    country: str
    state: str
    city: str
    latitude: float
    longitude: float
    severity: str
    status: str
    description: Optional[str]
    source: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True