from typing import List
from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
import bcrypt

from blog import models,schemas
from blog.database import SessionLocal,engine



models.Base.metadata.create_all(bind=engine)


app=FastAPI(debug=True)

#Dependency
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()






#create a blog

@app.post('/blog', response_model=schemas.Blog, status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.BlogModel(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return schemas.Blog.from_orm(new_blog)


#get all blogs

@app.get('/blogs', response_model=schemas.BlogListResponse, status_code=status.HTTP_200_OK)
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.BlogModel).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No blogs found')
    return schemas.BlogListResponse(message="Blogs found", data=[schemas.Blog.from_orm(blog) for blog in blogs])


#delete a blog

@app.delete('/blog/{id}',status_code=status.HTTP_200_OK)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    db.delete(blog)
    db.commit()
    return {"message": f"Blog with id {id} deleted successfully"}

#update a blog
@app.patch('/blog/{id}', response_model=schemas.Blog, status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.BlogCreate, db: Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    blog.update(dict(request))
    db.commit()
    return schemas.Blog.from_orm(blog.first())


#get a blog by Id

@app.get('/blog/{id}', response_model=schemas.Blog, status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    return schemas.Blog.from_orm(blog)



# #get all users

# @app.get("/users", response_model=schemas.User, status_code=status.HTTP_200_OK)
# def get_users(db: Session = Depends(get_db)):
#     try:
#         users = db.query(models.User).all()
#         if users == []:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
#         return {"message": "Users found", "data": users}
#     except:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")

#create user
        
# @app.post('/register',response_model=schemas.User,status_code=status.HTTP_201_CREATED)
# def create_user(request:schemas.User,db:Session=Depends(get_db)):
#     new_user=models.User(username=request.username,
#                          email=request.email,
#                          password=bcrypt.hashpw(request.password.encode('utf-8'),bcrypt.gensalt()))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {"message":"User created successfully","data":new_user}