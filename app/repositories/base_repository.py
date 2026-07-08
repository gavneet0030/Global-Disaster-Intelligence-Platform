from sqlalchemy.orm import Session


class BaseRepository:

    def __init__(
        self,
        model
    ):
        self.model = model

    def create(
        self,
        db: Session,
        obj
    ):

        db.add(obj)
        db.commit()
        db.refresh(obj)

        return obj

    def get_all(
        self,
        db: Session
    ):

        return db.query(self.model).all()

    def get_by_id(
        self,
        db: Session,
        obj_id: int
    ):

        return (
            db.query(self.model)
            .filter(
                self.model.id == obj_id
            )
            .first()
        )

    def delete(
        self,
        db: Session,
        obj_id: int
    ):

        obj = self.get_by_id(
            db,
            obj_id
        )

        if obj:

            db.delete(obj)
            db.commit()

        return obj

    def count(
        self,
        db: Session
    ):

        return (
            db.query(self.model)
            .count()
        )