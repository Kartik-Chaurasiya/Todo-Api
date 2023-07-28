from sqlalchemy.orm import Session
from db.models.todo import Todo
from pydantic_models.todo import TodoCreate, TodoSearch
from fastapi import HTTPException, status
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

def todo_search(db: Session, todo: TodoSearch, user, skip: int = 0, limit: int = 100):
    query = db.query(Todo)

    if todo.todo_name:
        query = query.filter(Todo.todo_name == todo.todo_name)
    
    if todo.complete_by:
        query = query.filter(Todo.complete_by == todo.complete_by)
    
    if todo.created_at:
        query = query.filter(Todo.created_at == todo.created_at)
    
    if todo.priority:
        query = query.filter(Todo.priority == todo.priority)

    if todo.completed:
        query = query.filter(Todo.completed == todo.completed)

    query = query.filter(Todo.user_id == user.id)
    query = query.filter(Todo.is_active == True)
    query = query.offset(skip).limit(limit)
    todos = query.all()
    return todos

def mark_todos_as_completed(db: Session, todo_ids, user):
    updated_todos = []
    for todo_id in todo_ids:
        todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
        if todo:
            # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo not found")

            todo.completed = True
            db.commit()
            updated_todos.append(todo)

    if len(updated_todos) != len(todo_ids):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Some todos could not be updated")

    return {"message": "Todos marked as completed"}

def deactivate_todo_by_id(db, todo_id, user):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo not found")

    # Deactivate the todo by setting is_active to False
    todo.is_active = False
    db.commit()

    return {"message": f"Todo has been deleted"}