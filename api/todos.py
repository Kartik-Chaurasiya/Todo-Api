from typing import Optional, List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from api.utils.todos import get_todos, create_todos
from db.db_setup import get_db
from pydantic_models.todo import TodoBase, TodoResponse, TodoCreate
from api.utils import oauth2
from pydantic_models.user import User

router = APIRouter(
    prefix="/todos",
    tags=['Todo']
)

@router.get("", response_model=List[TodoResponse])
async def get_all_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = get_todos(db, skip = skip, limit = limit)
    return todos

# @router.post("", status_code=status.HTTP_201_CREATED, response_model=TodoResponse)
# async def create_new_user(todos: CreateTodo, db: Session = Depends(get_db), user: int = Depends(oauth2.get_current_user)):
#     return create_todos(db, todos, user)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=TodoResponse)
async def create_new_user(todos: TodoCreate, db: Session = Depends(get_db), user: User = Depends(oauth2.get_current_user)):
    data = create_todos(db, todos, user)
    print("API Response:", data)
    return data


