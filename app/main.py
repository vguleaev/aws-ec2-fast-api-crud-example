from fastapi import FastAPI, HTTPException
from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate
from app.crud import todo_crud

app = FastAPI()


@app.get("/todos/", response_model=list[Todo])
async def read_todos():
    return todo_crud.read_todos()


@app.post("/todos/", response_model=Todo)
async def create_todo(todo: TodoCreate):
    return todo_crud.create_todo(todo)


@app.get("/todos/{todo_id}", response_model=Todo)
async def read_todo(todo_id: int):
    todo = todo_crud.read_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: TodoUpdate):
    updated_todo = todo_crud.update_todo(todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo


@app.delete("/todos/{todo_id}", response_model=dict)
async def delete_todo(todo_id: int):
    if not todo_crud.delete_todo(todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
