from fastapi import FastAPI
from service.products import get_all_products

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to fastapi."}

@app.get("/products")
def get_products():
    return get_all_products