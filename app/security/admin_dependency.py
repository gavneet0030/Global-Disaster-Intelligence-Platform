from fastapi import Depends, HTTPException

from app.security.dependencies import get_current_user


def admin_required(
    user=Depends(get_current_user)
):

    if not user.get("is_admin", False):

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return user