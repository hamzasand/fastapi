# Simple get route in fastapi
from fastapi import FastAPI

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
def get_users(name: str=None, price: int=10):
    return {
        "name":name,
        "price": price
    }
