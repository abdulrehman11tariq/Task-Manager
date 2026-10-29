from fastapi import APIRouter, Depends , status, Request
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

@url_router.get("/is_authenticated" , status_code = status.HTTP_200_OK)
def is_authenticated(request: Request , db: Session = Depends(get_db) , response_model = userResponseSchema):
    return controller.is_authenticated(request, db)