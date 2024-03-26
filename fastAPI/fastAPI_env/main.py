from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from blog import models, schemas
from blog.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blogs")
def post_blog(request:schemas.Blog):
    return request


#https://fastapi.tiangolo.com/tutorial/sql-databases/#main-fastapi-app

