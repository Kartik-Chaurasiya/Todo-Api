from typing import Optional, List
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel

router = APIRouter()
current_id = 1

users = []

class UserBase(BaseModel):
    username: str
    email_id: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.get("/user/{id}", response_model=User)
async def get_user_by_id(id: int):
    user = next((user for user in users if user.id == id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=User)
async def create_user(user: UserCreate):
    global current_id
    new_user = User(id=current_id, **user.model_dump())
    current_id += 1
    users.append(new_user)
    return new_user

@router.put("/user/{id}", response_model=User)
async def update_user(id: int, user: UserCreate):
    existing_user = next((user for user in users if user.id == id), None)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    existing_user.username = user.username
    existing_user.email_id = user.email_id
    existing_user.password = user.password
    return existing_user

@router.delete("/user/{id}")
async def delete_user(id: int):
    global users
    users = [user for user in users if user.id != id]
    return {"message": "User deleted successfully"}
    
