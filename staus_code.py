from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.post("/create_user",status_code= status.HTTP_201_CREATED)
def user_create():
    return {
        "message": "user created"
    }

@app.get("/users")
def user_get():
    return {
        "status":"sucess",
        "message": "user data fetched",
        "data": {
            "name": "Hamza",
            "age": 23
        }
    }

@app.get("/user/{user_id}")
def user_getid(user_id:int):
    if user_id != 1:
        raise Exception(
            status_code = 404,
            detail= "user did not exist"
        )
    return {
        "id": 1,
        "name": "Hamza"
    }
