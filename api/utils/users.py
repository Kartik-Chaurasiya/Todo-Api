from sqlalchemy.orm import Session
from db.models.user import User
from pydantic_models.user import UserCreate
from fastapi import HTTPException
from api.utils.utils import hash, is_valid_email, is_valid_password

def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id, User.is_active == True).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    # Check if the email is valid
    if not is_valid_email(user.email_id):
        raise HTTPException(status_code=400, detail="Invalid email format")

    # Check if the password is valid
    if not is_valid_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid password format. Password must have at least 12 characters and contain numbers and special characters.")

    # Check if a user with the same username or email already exists
    existing_user = db.query(User).filter(User.username == user.username, User.email_id == user.email_id).first()

    if existing_user:
        # If user with the same email and username exists
        if existing_user.is_active:
            # User is already activated
            raise HTTPException(status_code=400, detail="User with the same username and email is already present")
        else:
            # Set the user as activated and return a message
            existing_user.is_active = True
            db.commit()
            db.refresh(existing_user)
            return existing_user

    # Check if a user with the same username or email already exists
    existing_user = db.query(User).filter(User.username == user.username).first()
    existing_email = db.query(User).filter(User.email_id == user.email_id).first()
    if existing_user or existing_email:
        raise HTTPException(status_code=400, detail="User with the same username and email already exists")

    # If all checks pass, create the new user and add it to the database
    user.password = hash(user.password)
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def deactivate_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    user.is_active = False
    db.commit()
    return {"message": "User deactivated successfully"}


