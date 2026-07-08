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
            .filter(
                model.event_id == event_id
            )
            .first()
        ) is not None