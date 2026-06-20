from fastapi import FastAPI, Query, HTTPException
from service.products import get_all_products


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to fastapi."}

# @app.get("/products")
# def get_products():
#     return get_all_products

@app.get("/products")
def list_products(
    name: str = Query(
        default=None,
        min_length =1,
        max_length =20,
        description="search product by name (case insenstive)"
    ),
    sort_by_price: bool =Query(default=False, description="Sort products by price"),
    order: str=Query(
        default="asc", description="Sort order when sort_by_price=true (asc,desc)"
    )

):
    products = get_all_products()

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    if not products:
        raise HTTPException(
            status_code = 404, detail=f"no product found matching name={name}"
        )
    
    if sort_by_price:
        reverse = order == "desc"
        products = sorted(products, key=lambda p: p.get("price",0), reverse=reverse)
        
    total = len(products)

    return {"total":total,"item":products}