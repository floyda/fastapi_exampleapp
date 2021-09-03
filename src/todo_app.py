from datetime import datetime
from uuid import uuid1

from pydantic import BaseModel


class TodoNote(BaseModel):
    id: str
    note: str = ""
    created: datetime
    completed: bool


class TodoApp:
    def __init__(self) -> None:
        pass

    def get_all(self):
        return {"todos": [
            TodoNote(
                id=str(uuid1()),
                note="Must ring Dad",
                created=datetime.now(),
                completed=False
            )
        ]}
