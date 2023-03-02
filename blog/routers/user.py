from fastapi import APIRouter, Depends,HTTPException,status
from ..hashing import Hash
from .. import schemas, models, database
from sqlalchemy.orm import Session
from blog.database import SessionLocal
from ..respository import user
from . import oauth2


router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db = database.get_db

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db: SessionLocal = Depends(get_db)):
    return user.create(db,request)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    return user