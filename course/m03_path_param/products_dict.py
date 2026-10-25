from typing import Any
from fastapi import FastAPI

app = FastAPI()

products = {
    1001: {"name": "Wireless Mouse", "price": 18.99, "stock": 42},
    1002: {"name": "Mechanical Keyboard", "price": 64.99, "stock": 18},
    1003: {"name": "USB-C Hub", "price": 29.99, "stock": 35},
    1004: {"name": "Laptop Stand", "price": 39.99, "stock": 12},
    1005: {"name": "Webcam", "price": 54.99, "stock": 25},
    1006: {"name": "Bluetooth Speaker", "price": 44.99, "stock": 30},
    1007: {"name": "External SSD", "price": 89.99, "stock": 10},
}


@app.get("/product/latest")
def get_latest_product() -> dict[str, Any]:
    id = max(products.keys())
    return products[id]

@app.get("/product/{id}")
def get_product(id : int) -> dict[str, Any]:
    if id not in products:
        return {"details": "Given id does not exist"}
    return products[id]
