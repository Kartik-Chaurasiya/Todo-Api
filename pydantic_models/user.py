from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email_id: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True