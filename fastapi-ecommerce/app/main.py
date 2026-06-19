from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to fastapi."}

@app.get("/products/{id}")
def get_products(id: int):
    products = ['brush', "laptop","mouse","monitor"]
    return products[id]