from app.models import Todo, todos
from app.schemas import TodoCreate, TodoUpdate


class TodoCRUD:
    def __init__(self):
        self.counter = 1

    def create_todo(self, todo_data: TodoCreate) -> Todo:
        todo = Todo(id=self.counter, **todo_data.model_dump())
        todos.append(todo)
        self.counter += 1
        return todo

    def read_todos(self) -> list[Todo]:
        return todos

    def read_todo(self, todo_id: int) -> Todo | None:
        for todo in todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, todo_data: TodoUpdate) -> Todo | None:
        todo = self.read_todo(todo_id)
        if not todo:
            return None
        updated_todo = todo.model_copy(update=todo_data.model_dump())
        todos[todos.index(todo)] = updated_todo
        return updated_todo

    def delete_todo(self, todo_id: int) -> bool:
        global todos
        todo = self.read_todo(todo_id)
        if not todo:
            return False
        todos = [todo for todo in todos if todo.id != todo_id]
        return True


todo_crud = TodoCRUD()
