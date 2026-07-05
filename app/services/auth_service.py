from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import LoginRequest
from app.core.security import (
    verify_password,
    create_access_token
)


def login_user(
    db: Session,
    login: LoginRequest
):

    user = (
        db.query(User)
        .filter(User.email == login.email)
        .first()
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