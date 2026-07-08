from sqlalchemy.orm import Session

from app.schemas.user import UserCreate

from app.repositories.user_repository import (
    user_repository
)


class UserService:

    @staticmethod
    def create_user(
        db: Session,
        user: UserCreate
    ):

        existing = user_repository.get_by_email(
            db,
            user.email
        )

        if existing:

            return None

        return user_repository.create_user(
            db,
            user
        )

    @staticmethod
    def get_all_users(
        db: Session
    ):

        return user_repository.get_all(db)

    @staticmethod
    def get_user_by_id(
        db: Session,
        user_id: int
    ):

        return user_repository.get_by_id(
            db,
            user_id
        )

    @staticmethod
    def delete_user(
        db: Session,
        user_id: int
    ):

        return user_repository.delete(
            db,
            user_id
        )