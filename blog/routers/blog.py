from fastapi import APIRouter, Depends, HTTPException, Response, status
from .. import schemas, database
from sqlalchemy.orm import Session
from typing import List
from ..respository import blog
from . import oauth2

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db

@router.get("/", response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(db, request)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db:Session= Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def show(id ,db:Session =Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)