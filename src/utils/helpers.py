from fastapi import Request, HTTPException , status , Depends
from sqlalchemy.orm import Session
from src.utils.setting import settings
import jwt
from jwt.exceptions import InvalidTokenError
from src.user.models import UserModel
from src.utils.db import get_db



def is_authenticated(request: Request , db: Session = Depends(get_db)):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header is missing")

    token = auth_header.split(" ")[-1]

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    userid = payload.get("_id")
    if not userid:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(UserModel).filter(UserModel.id == userid).first()
    if not user:
        raise HTTPException(status_code=401, detail="User is invalid")

    return {"id": user.id, "username": user.username, "email": user.email}