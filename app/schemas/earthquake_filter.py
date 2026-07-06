from pydantic import BaseModel


class MagnitudeFilter(BaseModel):

    minimum: float