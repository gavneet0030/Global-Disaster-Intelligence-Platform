from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest

from app.core.security import (
    verify_password,
    create_access_token
)


class AuthService:

    @staticmethod
    def login(
        db: Session,
        login: LoginRequest
    ):

        user = UserRepository.get_by_email(
            db,
            login.email
        )

        if user is None:
            return None

        if not verify_password(
            login.password,
            user.password
        ):
            return None

        token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }