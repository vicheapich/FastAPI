from fastapi import Depends, Request, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog import database
from .. import models, schemas
from fastapi.security import OAuth2PasswordBearer
from .import token
from ..respository import user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(data: str = Depends(oauth2_scheme), db: database.SessionLocal = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    #check blacklist token
    used_black_list = user.find_black_list_token(data, db)
    if used_black_list:
        raise credentials_exception

    return token.verify_token(data, credentials_exception)

def get_token_user(token:str = Depends(oauth2_scheme)):
    return token

# def get_current_active_user(request: Request):
#     current_user = request.cookies.get("username")
#     if not current_user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive user")