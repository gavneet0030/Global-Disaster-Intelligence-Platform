from fastapi import APIRouter, Depends

from app.security.dependencies import get_current_user

from app.schemas.profile import (
    ProfileResponse
)

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.get(
    "/me",
    response_model=ProfileResponse
)
def my_profile(
    user=Depends(get_current_user)
):

    return {

        "email": user["sub"]

    }