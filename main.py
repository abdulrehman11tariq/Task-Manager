from fastapi import FastAPI
from src.utils.db import base, engine
from src.tasks.models import Task
from src.tasks.router import task_routes

base.metadata.create_all(engine)

app = FastAPI(title="FastAPI with SQLAlchemy", version="1.0.0")

app.include_router(task_routes)


