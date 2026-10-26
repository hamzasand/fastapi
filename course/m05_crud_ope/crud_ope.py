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

# invalid id exception
def get_or_404(id: int) -> dict[str, Any]:
    if id not in products:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Product wit given id did not exists",
        )
    return products[id]

## Read
@app.get("/product")
def get_product(id: int) -> dict[str, Any]:
    return get_or_404(id)

## Create
@app.post("/product")
def create_product(name: str, price: int, stock: int) -> dict[str, int]:
    if price <= 0:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, "Price should be grater than 0",)
    if stock < 0:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, "Stock should be greater than 0")

    new_id = max(products.keys()) + 1
    products[new_id] = {"name": name, "price": price, "stock": stock}
    return {"id": new_id}

### UPDATE (replace everything) - every field is required
@app.put("/product")
def replace_product(
    id: int, name: str, price: float, stock: int,
) -> dict[str, Any]:
    get_or_404(id)
    products[id] = {"name": name, "price": price, "stock":stock}
    return products[id]

### DELETE
@app.delete("/product")
def delete_product(id: int) -> dict[str, str]:
    get_or_404(id)
    products.pop(id)
    return {"detai": f"product with id{id} deleted"}