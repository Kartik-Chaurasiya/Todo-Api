from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import List

class TodoBase(BaseModel): 
    todo_name: str
    todo_desc: str
    priority: int = 1
    complete_by: date

class TodoCreate(TodoBase):
    completed: bool = False
    is_active: bool = True

class TodoResponse(TodoBase):
    id: int
    user_id: int
    completed: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime = False

    class Config:
        from_attributes = True

class TodoListResponse(BaseModel):
    todos: List[TodoResponse]

    class Config:
        from_attributes = True
    
class TodoSearch(BaseModel):
    todo_name: str = Field(None, title="Todo Name")
    complete_by: date = Field(None, title="Complete By Date")
    created_at: date = Field(None, title="Todo Date")
    priority: int = Field(None, title="Todo Priority")
    completed: bool = Field(None, title="Todo Completed")

class TodoComplete(BaseModel):
    id: List[int] = Field(None, title="Todo IDs")