from src.user.dtos import userSchema
from sqlalchemy.orm import Session

def register(body: userSchema, db: Session):
    print(body)
    return {"message": "User registered successfully"}