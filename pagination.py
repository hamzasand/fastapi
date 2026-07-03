from fastapi import FastAPI 
app = FastAPI()

users = [f"User {i}" for i in range(1,101)]

@app.get("/users")
def get_users(skip:int=0, limit:int=10):
    return users[skip: skip+limit]