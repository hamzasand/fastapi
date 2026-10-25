from fastapi import FastAPI

app = FastAPI(title = "Product Store API")

@app.get("/")
def home():
    return {"message":"Product API is running"}

@app.get("/product")
def get_product():
    return {"name": "Wireless Mouse", "price": 18.99, "stock":42}

