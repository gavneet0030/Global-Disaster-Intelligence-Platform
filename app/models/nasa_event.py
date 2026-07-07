from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from app.database.database import Base


class NASAEvent(Base):

    __tablename__ = "nasa_events"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nasa_id = Column(
        String,
        unique=True
    )

    title = Column(String)

    category = Column(String)

    latitude = Column(Float)

    longitude = Column(Float)

    date = Column(String)
    