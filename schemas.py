from pydantic import BaseModel, Field, EmailStr

from models import UserRole

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    role: UserRole = UserRole.USER