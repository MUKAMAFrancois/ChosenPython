from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
import bcrypt

from blog import models,schemas,database
from blog.database import SessionLocal,engine


models.Base.metadata.create_all(bind=engine)


app=FastAPI()

#Dependency
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



#create user
        
@app.post('/register',response_model=schemas.User,status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    new_user=models.User(username=request.username,
                         email=request.email,
                         password=bcrypt.hashpw(request.password.encode('utf-8'),bcrypt.gensalt()))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User created successfully","data":new_user}


#create a blog

@app.post('/blog',response_model=schemas.Blog,status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,
                         body=request.body
                         )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"message":"Blog created successfully","data":new_blog}

#get all blogs

@app.get('/blogs',response_model=schemas.Blog,status_code=status.HTTP_200_OK)
def get_blogs(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    if blogs==[]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No blogs found')
    return {"message":"Blogs found","data":blogs}

#get all users
@app.get("/users", response_model=schemas.User, status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    try:
        users = db.query(models.User).all()
        if users == []:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
        return {"message": "Users found", "data": users}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")