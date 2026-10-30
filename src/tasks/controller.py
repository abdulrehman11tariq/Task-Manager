from src.tasks.dtos import TaskCreate
from sqlalchemy.orm import Session
from src.tasks.models import Task
from fastapi import HTTPException, status
from src.utils.helpers import is_authenticated

def create_task(tasks: TaskCreate, db: Session):

    data = tasks.model_dump()


    new_task = Task(title = data['title'], description = data['description'], completed = data['completed'])

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_tasks(db: Session):

    tasks = db.query(Task).all()
    
    return tasks


def get_one_task(db: Session , task_id: int):

    task = db.get(Task , task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

def update_task(db: Session , task_id: int, body:TaskCreate):

    task = db.get(Task , task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = body.title
    task.description = body.description
    task.completed = body.completed

    db.add(task)
    db.commit()
    db.refresh(task)


    return task

def delete_task(db: Session , task_id: int):

    task = db.get(Task , task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

   
    db.delete(task)
    db.commit()
    db.refresh(task)

    return None
