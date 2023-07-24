from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from api.utils import oauth2, utils
from db.db_setup import engine, get_db
from sqlalchemy.orm import Session
from db.models.user import User
from pydantic_models import user

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=user.Token)
def login(user_data : OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(get_db)):
    users = db.query(User).filter(User.username == user_data.username).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    if not utils.verify(user_data.password, users.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    #create token
    access_token = oauth2.create_access_token(data = {"id" : users.id})

    return {"access_token" : access_token, "token_type" : "bearer"}