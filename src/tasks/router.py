from fastapi import APIRouter, Depends
from src.tasks.controller import create_task, get_tasks
from src.tasks.dtos import TaskCreate
from src.utils.db import get_db


task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task_endpoint(task: TaskCreate , db = Depends(get_db)):
    return create_task(task , db)

@task_routes.get("/all_tasks")
def get_tasks_endpoint(db = Depends(get_db)):

    return get_tasks(db)