from typing import Optional, List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from api.utils.todos import get_todos, create_todos, todo_search, mark_todos_as_completed, deactivate_todo_by_id
from db.db_setup import get_db
from pydantic_models.todo import TodoBase, TodoResponse, TodoCreate, TodoSearch, TodoComplete
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

@router.post("", status_code=status.HTTP_201_CREATED, response_model=TodoResponse)
async def create_new_user(todos: TodoCreate, db: Session = Depends(get_db), user: User = Depends(oauth2.get_current_user)):
    data = create_todos(db, todos, user)
    print("API Response:", data)
    return data

@router.post("/search", status_code=status.HTTP_200_OK, response_model=List[TodoResponse])
async def get_all_todos(todo: TodoSearch, skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user: User = Depends(oauth2.get_current_user)):
    return todo_search(db, todo, user, skip = skip, limit = limit)

@router.put("", status_code=status.HTTP_200_OK)
async def mark_todos_as_complete(todo_ids: TodoComplete, db: Session = Depends(get_db), user: User = Depends(oauth2.get_current_user)):
    # Update todos with the specified IDs and belonging to the authenticated user
    if len(todo_ids.id) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No todo IDs provided")
    else:
        return mark_todos_as_completed(db, todo_ids.id, user)
    
@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def deactivate_todo(id: int, db: Session = Depends(get_db), user: User = Depends(oauth2.get_current_user)):
    return deactivate_todo_by_id(db, id, user)


     


