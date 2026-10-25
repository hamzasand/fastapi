from typing import Any
from fastapi import FastAPI

app = FastAPI()

@app.get("/product/latest")  # First path always set first
def get_latest_product() -> dict[str, Any]:
    return {"id": 1007, "name": "External SSD", "price": 89.99, "stock": 10}

@app.get("/product/{id}")
def get_product(id: int) -> dict[str, Any]:
    return {"id": id, "name": "Wireless Mouse", "price": 18.99, "stcok": 42}