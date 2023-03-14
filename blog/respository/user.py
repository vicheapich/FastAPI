from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from .. import models, schemas, hashing


def create(db:Session, request:schemas.Blog):
    new_user = models.User(name=request.name, email=request.email, password =hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    return user

def find_black_list_token(token:str, db:Session):
    used_token = db.query(models.Blacklist).filter(models.Blacklist.token == token).first()
    return used_token

def save_black_list_token(token:str, db:Session, current_user = models.User.email):
    # block_token = db.query(token = token, email= current_user.email)
    block_token = models.Blacklist(token = token, email=current_user)
    db.add(block_token)
    db.commit()
    db.refresh(block_token)
    return block_token
