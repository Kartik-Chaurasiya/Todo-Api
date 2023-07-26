from pydantic import BaseModel
from datetime import datetime
from datetime import date, datetime

# class TodoBase(BaseModel):
#     todo_name : str
#     todo_desc : str
#     complete_by : date
#     priority : int = 1

# class CreateTodo(TodoBase):
#     completed : bool = False
#     is_active: bool = True

# class TodoResponse(TodoBase):
#     id : int
#     user_id : int
#     completed : bool
#     is_active : bool
#     created_at : datetime
#     updated_at : datetime

#     class Config:
#         from_attributes = True

from pydantic import BaseModel, conlist
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