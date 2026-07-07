from pydantic import BaseModel


class NASAEventResponse(BaseModel):

    id: int

    nasa_id: str

    title: str

    category: str

    latitude: float

    longitude: float

    date: str

    class Config:

        from_attributes = True