from sqlalchemy.orm import Session
from db.models.todo import Todo
from pydantic_models.todo import TodoCreate
from fastapi import HTTPException
from sqlalchemy import and_
from datetime import date, timedelta, datetime
# from api.utils.utils import 

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()

def create_todos(db: Session, todo: TodoCreate, user):
    
    # Get today's date
    today_date = date.today()
    updated_at = datetime.utcnow()

    # Check if a Todo with the same todo_name, created_at (matching today's date), and user_id already exists
    existing_todo = db.query(Todo).filter(
        and_(
            Todo.todo_name == todo.todo_name,
            Todo.created_at >= today_date,
            Todo.created_at < today_date + timedelta(days=1),
            Todo.user_id == user.id
        )
    ).first()

    if existing_todo:
        # If a Todo with the same attributes exists, raise an exception or handle as needed
        # For example, you can return an error message or raise an HTTPException
        raise HTTPException(status_code=400, detail="A Todo with the same name, created date, and user ID already exists")

    # If no existing Todo found, create the new Todo and add it to the database
    new_todo = Todo(user_id = user.id, updated_at=updated_at, **todo.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo