from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("create_user")
def creat_user(user: User):
    return {
        "message": "user created sucesfully",
        "user_inf": user
    }