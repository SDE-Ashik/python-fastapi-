from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: str
    address: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: str
