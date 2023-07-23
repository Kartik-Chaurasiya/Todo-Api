from typing import Optional, List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from api.utils.users import create_user, get_user, get_user_by_email, get_users, deactivate_user
from db.db_setup import get_db
from pydantic_models.user import UserCreate, UserBase, User, UserResponse

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.get("", response_model=List[User])
async def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip = skip, limit = limit)
    return users

@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_new_user(users: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, users)

@router.get("/{id}", status_code=status.HTTP_200_OK , response_model=UserResponse)
async def get_user_id(id : int, db: Session = Depends(get_db)):
    return get_user(db, id)

@router.delete("/{id}")
async def delete_user(id: int, db: Session = Depends(get_db)):
    return deactivate_user(db, id)
