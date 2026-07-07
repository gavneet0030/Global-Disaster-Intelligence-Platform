from sqlalchemy.orm import Session

from app.models.nasa_event import NASAEvent


def save_events(
    db: Session,
    events
):

    inserted = 0

    for event in events:

        exists = (

            db.query(NASAEvent)

            .filter(

                NASAEvent.nasa_id == event["id"]

            )

            .first()

        )

        if exists:
            continue

        new_event = NASAEvent(

            nasa_id=event["id"],

            title=event["title"],

            category=event["category"],

            latitude=event["latitude"],

            longitude=event["longitude"],

            date=event["date"]

        )

        db.add(new_event)

        inserted += 1

    db.commit()

    return inserted


def get_events(
    db: Session
):

    return (

        db.query(NASAEvent)

        .order_by(

            NASAEvent.id.desc()

        )

        .all()

    )