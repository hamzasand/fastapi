# Simple get route in fastapi
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from fasapi"}