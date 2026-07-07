from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    is_admin: bool = False


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    is_admin: bool

    class Config:
        from_attributes = True