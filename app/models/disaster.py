from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from app.database.database import Base


class Disaster(Base):

    __tablename__ = "disasters"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    disaster_type = Column(
        String(100),
        nullable=False
    )

    country = Column(
        String(100),
        nullable=False
    )

    state = Column(
        String(100),
        nullable=False
    )

    city = Column(
        String(100),
        nullable=False
    )

    latitude = Column(
        Float,
        nullable=False
    )

    longitude = Column(
        Float,
        nullable=False
    )

    severity = Column(
        String(50),
        nullable=False
    )

    status = Column(
        String(50),
        default="Active"
    )

    description = Column(
        String(500)
    )

    source = Column(
        String(100),
        default="Manual"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )