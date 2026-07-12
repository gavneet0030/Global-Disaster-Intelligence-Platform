from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)

from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    login: LoginRequest,
    db: Session = Depends(get_db)
):

    token = AuthService.login(
        db,
        login
    )

    if token is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return token