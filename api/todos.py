from typing import Optional, List
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

todos = []

# Model for the Todo item
class TodoCreate(BaseModel):
    todo_name: str
    todo_desc: str
    priority: int

class TodoUpdate(BaseModel):
    todo_name: str
    todo_desc: str
    priority: int

class Todo(TodoCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# API endpoint to get all todo items
@router.get("/todos", response_model=List[Todo])
def get_all_todos():
    return todos

# API endpoint to create a new todo item
@router.post("/todos", response_model=Todo)
def create_todo_item(todo: TodoCreate):
    todo_dict = todo.model_dump()
    todo_dict["id"] = len(todos) + 1
    todo_dict["created_at"] = datetime.now()
    todo_dict["updated_at"] = datetime.now()
    todos.append(todo_dict)
    return todo_dict

# API endpoint to get a specific todo item by ID
@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo_item(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo item not found")

# API endpoint to update a specific todo item by ID
@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo_item(todo_id: int, todo: TodoUpdate):
    for item in todos:
        if item["id"] == todo_id:
            item.update(todo.dict(exclude_unset=True))
            item["updated_at"] = datetime.now()
            return item
    raise HTTPException(status_code=404, detail="Todo item not found")

# API endpoint to delete a specific todo item by ID
@router.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int):
    for index, item in enumerate(todos):
        if item["id"] == todo_id:
            todos.pop(index)
            return {"message": "Todo item deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo item not found")
