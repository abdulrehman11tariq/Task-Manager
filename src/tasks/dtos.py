from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False

class TaskOut(TaskCreate):
    id: int

    title: str
    description: str
    completed: bool = False
    user_id: int | None  = 0