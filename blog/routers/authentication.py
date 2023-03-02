
from fastapi import APIRouter,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from . import token

router = APIRouter(
    tags = ['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"USER is NOT FOUND.")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= f"Incorrect Password.")

    
    access_token = token.create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}