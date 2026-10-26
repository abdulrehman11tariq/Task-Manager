from sqlalchemy import Column, Integer, String , Boolean , DateTime
from src.utils.db import base

class UserModel(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hash_password = Column(String, nullable=False)
