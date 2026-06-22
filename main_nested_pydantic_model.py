from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Adress(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    adress: Adress

@app.post("/create_user")
def add_user(user: User):
    return {
        "message": "User created sucefully",
        "user_info": user
    }
