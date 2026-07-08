from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

from app.repositories.base_repository import BaseRepository


class UserRepository(
    BaseRepository
):

    def __init__(self):

        super().__init__(User)

    def get_by_email(
        self,
        db: Session,
        email: str
    ):

        return (
            db.query(User)
            .filter(
                User.email == email
            )
            .first()
        )

    def create_user(
        self,
        db: Session,
        user: UserCreate
    ):

        db_user = User(

            full_name=user.full_name,

            email=user.email,

            password=hash_password(
                user.password
            )

        )

        return self.create(
            db,
            db_user
        )


user_repository = UserRepository()