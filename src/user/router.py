from fastapi import APIRouter, Depends , status
from sqlalchemy.orm import Session
from src.user.dtos import userSchema
from src.utils.db import get_db
from src.user import controller


url_router = APIRouter(prefix="/user")

@url_router.post("/register" , status_code = status.HTTP_201_CREATED)
def register(body: userSchema , db: Session = Depends(get_db)):
    return controller.register(body , db)
    
