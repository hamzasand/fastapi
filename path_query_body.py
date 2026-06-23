from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users_list = []

class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user:User):
    users_list.append(user)
    return {
        "message": "user created sucessfully",
        "user_data": user
    }

@app.put("/user/{user_id}")
def user_update(user_id:int, user:User, notify: bool=False):
    if user_id < len(users_list):
        users_list[user_id] = user
        return {
            "Message": "user upadet",
            "data": user,
            "Notify": notify
        }
    return {
        "message": "user didnot exist"
    }
