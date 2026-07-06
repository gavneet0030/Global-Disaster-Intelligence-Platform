from pydantic import BaseModel


class EarthquakeResponse(BaseModel):

    id: int

    usgs_id: str

    place: str

    magnitude: float

    latitude: float

    longitude: float

    depth: float

    time: str

    class Config:

        from_attributes = True
        