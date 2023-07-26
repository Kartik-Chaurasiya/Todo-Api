from fastapi import FastAPI
from api import users, todos, auth
from db.db_setup import engine
from db.models import user, todo

user.Base.metadata.create_all(bind=engine)
todo.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ToDo API",
    description="Backend for a ToDo app.",
    version="0.0.1",
    contact={
        "name": "Kartik",
        "email": "kartikjchourasiya001@gmail.com",
    },
    license_info={
        "name": "MIT",
    }
)

app.include_router(users.router)
app.include_router(todos.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "ToDo API"}

