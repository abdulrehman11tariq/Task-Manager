from fastapi import FastAPI
from src.utils.db import base, engine

base.metadata.create_all(engine)

app = FastAPI(title="FastAPI with SQLAlchemy", version="1.0.0")


