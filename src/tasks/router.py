from fastapi import APIRouter
from src.tasks.controller import create_task


task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task_endpoint():
    return create_task()