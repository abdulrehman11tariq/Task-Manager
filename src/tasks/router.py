from fastapi import APIRouter, Depends , status
from src.tasks.controller import create_task, get_tasks , get_one_task , update_task , delete_task
from src.tasks.dtos import TaskCreate,TaskOut
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.models import UserModel


task_routes = APIRouter(prefix="/tasks")

#response moddel tells what will be returned we can limit the response using this (VALIDATOR)

@task_routes.post("/create" ,response_model=TaskOut, status_code = status.HTTP_201_CREATED)
def create_task_endpoint(task: TaskCreate , db: Session = Depends(get_db) , user = Depends(is_authenticated)):

    return create_task(task , db , user)


#status code 2xx is for success and 4xx is for client error , we can set these status codes using status.HTTP_200_OK
#here in the route

@task_routes.get("/all_tasks" , response_model=list[TaskOut], status_code = status.HTTP_200_OK)
def get_tasks_endpoint(db: Session = Depends(get_db) , user = Depends(is_authenticated)):

    return get_tasks(db)


@task_routes.get("/get_task/{task_id}" , response_model=TaskOut, status_code = status.HTTP_200_OK)
def get_one_task_endpoint(task_id: int , db: Session = Depends(get_db) , user = Depends(is_authenticated)):

    return get_one_task(db , task_id)

@task_routes.put("/update_task/{task_id}" , response_model=TaskOut, status_code = status.HTTP_201_CREATED)
def update_task_endpoint(task_id: int , body: TaskCreate , db: Session = Depends(get_db) , user = Depends(is_authenticated)):

    return update_task(db , task_id , body)

@task_routes.delete("/delete_task/{task_id}" , response_model=None, status_code = status.HTTP_204_NO_CONTENT)
def delete_task_endpoint(task_id: int , db: Session = Depends(get_db) , user = Depends(is_authenticated)):

    return delete_task(db , task_id)