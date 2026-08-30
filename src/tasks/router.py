from fastapi import APIRouter, Depends
from src.tasks.controller import create_task
from src.tasks.dtos import TaskCreate
from src.utils.db import get_db


task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task_endpoint(task: TaskCreate , db = Depends(get_db)):
    return create_task(task , db)