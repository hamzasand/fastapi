from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
todo_list = []
class Todo(BaseModel):
    id: int
    title: str
    complete: bool

@app.post("/todo")
def create_todo(todo:Todo):
    todo_list.append(todo)
    return {"message":"Create user sucefully",
            "user_data": todo}

@app.get("/todos/{todo_id}")
def get_todos(todo_id:int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    return {"error": "todo dont exist"}

@app.put("todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index]=updated_todo
            return{
                "message":"Data Updated",
                "data": updated_todo
            }
    return {"error":"Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message":"Data Deleted"}
    return {"error":"Todo not found"}
    
