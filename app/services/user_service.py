from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

from app.security.password_handler import hash_password


def create_user(
    db: Session,
    user: UserCreate
):

    db_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hash_password(user.password),
        is_admin=user.is_admin
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user