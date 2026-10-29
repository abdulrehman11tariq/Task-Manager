from fastapi import HTTPException
from src.user.dtos import userSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.utils.setting import settings
from pwdlib import PasswordHash
from datetime import datetime , timedelta
import jwt


pass_hash = PasswordHash.recommended()

def get_hash_pass(password):
    return pass_hash.hash(password);

def verify(password, hash_pass):
    return pass_hash.verify(password, hash_pass)


def register(body: userSchema, db: Session):

    is_username = db.query(UserModel).filter(UserModel.username == body.username).first()
   
    if is_username:
        raise HTTPException(status_code=400, detail="Username already exists")

    is_usermail = db.query(UserModel).filter(UserModel.email == body.email).first()
   
    if is_usermail:
        raise HTTPException(status_code=400, detail="Email already exists")

    hash_pass = get_hash_pass(body.password)

    user = UserModel(name=body.name,
                     username = body.username ,
                    email=body.email ,
                     hash_password = hash_pass)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def login(body: loginSchema , db:Session):

    is_username = db.query(UserModel).filter(UserModel.username == body.username).first()
   
    if not is_username:
        raise HTTPException(status_code=400, detail="Username is invalid")

    if not verify(body.password , is_username.hash_password):
        raise HTTPException(status_code = 400 , detail= "Password is worng")

    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)

    token  = jwt.encode({"_id" : is_username.id , "exp" : exp_time } , settings.SECRET_KEY , settings.ALGORITHM)

    return {"token" : token}