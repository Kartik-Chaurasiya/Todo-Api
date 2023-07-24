from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Literal

class UserBase(BaseModel):
    username: str
    email_id: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    is_active: bool

class UserCreate(UserBase):
    password: str
    is_active: bool = True

class User(UserBase):
    id: int
    created_at: datetime
    is_active: bool

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    user_name : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id: Optional[str] = None
