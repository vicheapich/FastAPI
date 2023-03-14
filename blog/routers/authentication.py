
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from fastapi import APIRouter,Depends, HTTPException, Request, Response, status
from fastapi.encoders import jsonable_encoder
from werkzeug.security import check_password_hash
from blog.routers import oauth2
from blog.routers.oauth2 import get_current_user
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from . import token
from fastapi_jwt_auth import AuthJWT
router = APIRouter(
    tags = ['Authentication']
)


@router.post('/login')
def login(response: Response, request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    response.set_cookie(key="username", value=user.email)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"USER is NOT FOUND.")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"Incorrect Password.")

    
    access_token = token.create_access_token(data={"sub": user.email})
    refresh_token = token.create_refresh_token(data={"sub": user.email})

    return {"access_token": access_token, "refresh_token": refresh_token ,"token_type": "bearer"}

@router.get('/refresh')
def refresh(request:Request):
    current_user = request.cookies.get("username")
    refresh_token = token.create_access_token(data={"sub": current_user})
    return {"access_token":refresh_token ,"token_type": "bearer"}

from ..respository import user
@router.get("/logout")
async def logout(request: Request ,token:str = Depends(oauth2.get_token_user), db: database.SessionLocal = Depends(database.get_db)):
    current_user = request.cookies.get("username")
    user.save_black_list_token(token ,db, current_user)
    return {
        "status_code ": status.HTTP_200_OK,
        "detail":"User logged out successfully."
    }
    