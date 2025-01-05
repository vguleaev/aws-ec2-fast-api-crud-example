from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool


class TodoUpdate(BaseModel):
    title: str
    description: str
    completed: bool
