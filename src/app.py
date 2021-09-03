from typing import List

from fastapi import FastAPI

from todo_app import TodoApp, TodoNote

api = FastAPI(
    title="TODO",
    description="Simple Todo project",
    version="0.0.1"
)

app = TodoApp()


@api.get("/todos")
async def get_all_todos() -> List[TodoNote]:
    return app.get_all()


@api.get("/todo/{todo_id}")
async def read_item(todo_id):
    return {"item_id": todo_id}
