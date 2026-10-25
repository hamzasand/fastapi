from typing import Any
from fastapi import FastAPI

app = FastAPI()

@app.get("/product/{id}")
def get_product(id: int) -> dict[str, Any]:

    return {
        "id": id,
        "name": "wireless Mouse",
        "price": 18.99,
        "stock": 42,
        
    }