from src.tasks.dtos import TaskCreate
from sqlalchemy.orm import Session
from src.tasks.models import Task

def create_task(tasks: TaskCreate, db: Session):

    data = tasks.model_dump()


    new_task = Task(title = data['title'], description = data['description'], completed = data['completed'])

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"message": "Task created successfully!", "task": new_task}

def get_tasks(db: Session):

    tasks = db.query(Task).all()
    
    return {"message": "Tasks retrieved successfully!", "tasks": tasks}