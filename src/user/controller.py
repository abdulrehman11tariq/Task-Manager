from fastapi import HTTPException
from src.user.dtos import userSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from pwdlib import PasswordHash


pass_hash = PasswordHash.recommended()

def get_hash_pass(password):
    return pass_hash.hash(password);


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