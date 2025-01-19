from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate
from app.db.db import engine
from sqlmodel import Session, select


class TodoCRUD:
    def __init__(self):
        self.counter = 1

    def create_todo(self, todo_data: TodoCreate) -> Todo:
        with Session(engine) as session:
            todo = Todo(**todo_data.model_dump())
            session.add(todo)
            session.commit()
            session.refresh(todo)
            return todo

    def read_todos(self) -> list[Todo]:
        with Session(engine) as session:
            statement = select(Todo)
            todos = list(session.exec(statement).all())
            return todos

    def read_todo(self, todo_id: int) -> Todo | None:
        with Session(engine) as session:
            statement = select(Todo).where(Todo.id == todo_id)
            todo = session.exec(statement).first()
            return todo

    def update_todo(self, todo_id: int, todo_data: TodoUpdate) -> Todo | None:
        with Session(engine) as session:
            statement = select(Todo).where(Todo.id == todo_id)
            todo = session.exec(statement).first()
            if not todo:
                return None

            todo.title = todo_data.title
            todo.description = todo_data.description
            todo.completed = todo_data.completed

            session.add(todo)
            session.commit()
            session.refresh(todo)
            return todo

    def delete_todo(self, todo_id: int) -> bool:
        with Session(engine) as session:
            statement = select(Todo).where(Todo.id == todo_id)
            todo = session.exec(statement).first()
            if not todo:
                return False

            session.delete(todo)
            session.commit()
            return True


todo_crud = TodoCRUD()
