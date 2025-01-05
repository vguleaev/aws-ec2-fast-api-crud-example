from typing import List
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool


# In-memory storage for Todos
todos: List[Todo] = []
