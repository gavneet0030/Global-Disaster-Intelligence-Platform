from sqlalchemy.orm import Session


class DuplicateChecker:

    @staticmethod
    def exists(
        db: Session,
        model,
        event_id: str
    ):

        return (
            db.query(model)
            .filter(model.event_id == event_id)
            .first()
        ) is not None

    @staticmethod
    def remove_duplicates(events):

        unique = []

        seen = set()

        for event in events:

            key = (
                round(event["latitude"], 2),
                round(event["longitude"], 2),
                event["title"].lower()
            )

            if key not in seen:

                seen.add(key)

                unique.append(event)

        return unique