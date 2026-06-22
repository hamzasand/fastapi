# Simple get route in fastapi
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from fasapi"}

# Dynamic route

@app.get("/user/{user_id}")
def get_user(user_id: str):
    return {"user_id": user_id}
