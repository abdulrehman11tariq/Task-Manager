from sqlalchemy import Column, Integer, String, Boolean , ForeignKey
from src.utils.db import base

class Task(base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))  # Foreign key to the User model
