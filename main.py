# Simple get route in fastapi
from fastapi import FastAPI, BaseModel

app= FastAPI()

# home route
@app.get("/")
def home():
    return {"message": "Hello from fasapi"}

# Dynamic route
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# querry parameters + Default value
@app.get("/items")
def get_users(name: str, price: int=10):
    return {
        "name":name,
        "price": price
    }

#post rrequest + request body + pydentic
class User(BaseModel):
    name: str
    age: int

@app.post("/create_user")
def create_user(user:User):
    return {
        "message": "user created sucssfully",
        "data": User
    }
