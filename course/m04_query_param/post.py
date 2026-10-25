from typing import Any
from fastapi import FastAPI, HTTPException, status

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


@app.get("/product")
def get_product(id: int) -> dict[str, Any]:
    if id not in products:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = "Product with id not found"
        )
    return products[id]

# Same URL as GET - different METHOD, so no clash
@app.post("/product")
def create_product(name: str, price: float, stock: int) -> dict[str, Any]:
    if price <= 0:
        raise HTTPException(
            status_code= status.HTTP_406_NOT_ACCEPTABLE,
            detail = "Product price should be greater 0",
        )

    new_id = max(products.keys()) + 1
    products[new_id] = {"name":name, "price":price, "stock":stock}
    return {"id": new_id}