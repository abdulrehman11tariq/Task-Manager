from fastapi import APIRouter, Depends , status
from sqlalchemy.orm import Session
from src.user.dtos import userSchema , userResponseSchema, loginSchema
from src.utils.db import get_db
from src.user import controller


url_router = APIRouter(prefix="/user")

@url_router.post("/register" , response_model = userResponseSchema , status_code = status.HTTP_201_CREATED)
def register(body: userSchema , db: Session = Depends(get_db)):
    return controller.register(body , db)
    
@url_router.post("/login" , status_code = status.HTTP_200_OK)
def login(body: loginSchema , db: Session = Depends(get_db)):
    return controller.login(body , db)