from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://username:password@localhost:5432/tododb"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)


Base.metadata.create_all(bind=engine)


class TodoCreate(BaseModel):
    title: str
    description: str


@app.post("/todos/")
def create_todo(todo: TodoCreate):
    db = SessionLocal()
    db_todo = Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    db.close()
    return db_todo


@app.get("/todos/")
def read_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return todos


@app.get("/todos/{todo_id}")
def read_todo(todo_id: int):
    db = SessionLocal()
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.close()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
