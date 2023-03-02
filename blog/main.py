from fastapi import FastAPI
from . import models
from .database import engine, get_db
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)



app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)






# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

#create blog by vichea on 01/03/2023
# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create(request:schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id= 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

#delete blog by vichea on 01/03/2023
# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
# def destroy(id, db:Session=Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id ==id).delete(synchronize_session=False)
#     db.commit()
#     return "Done"

#update blog by vichea on 01/03/2023
# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update(id, request: schemas.Blog, db:Session= Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blogs.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} not found")
#     blogs.update({'title':request.title, 'body':request.body})
#     db.commit()
#     return "updated"

#get_all blog by vichea on 01/03/2023
# @app.get("/blog", response_model=List[schemas.ShowBlog], tags=['blogs'])
# def all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


#show_all blog by vichea on 01/03/2023
# @app.get("/blog/{id}", status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog, tags=['blogs'])
# def show(id, response:Response ,db:Session =Depends(get_db)):
#     blog_id = db.query(models.Blog).filter(models.Blog.id ==id).first()
#     if not blog_id:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
#         # response.statu s_code = status.HTTP_404_NOT_FOUND
#         # return {'detail':f'Blog with the id {id} is not available'}
#     return blog_id


#create_user blog by vichea on 01/03/2023
# @app.post('/user',response_model=schemas.ShowUser,tags=['Users'])
# def create_user(request:schemas.User,db: Session = Depends(get_db)):
#     new_user = models.User(name=request.name, email=request.email, password =hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

#get_user blog by vichea on 01/03/2023
# @app.get('/user/{id}', response_model=schemas.ShowUser,tags=['Users'])
# def get_user(id:int, db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
#     return user
