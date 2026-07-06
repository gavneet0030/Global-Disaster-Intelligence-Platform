from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from app.database.database import Base


class Earthquake(Base):

    __tablename__ = "earthquakes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    usgs_id = Column(
        String,
        unique=True
    )

    place = Column(String)

    magnitude = Column(Float)

    latitude = Column(Float)

    longitude = Column(Float)

    depth = Column(Float)

    time = Column(String)