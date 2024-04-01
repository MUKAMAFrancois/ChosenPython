from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from blog import models,schemas
from blog.database import get_db
from .authentication import get_current_user

router = APIRouter(
    tags=["blogs"]
)


#create a blog


@router.post('/blog', response_model=schemas.Blog, status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogCreate, 
                db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    
    current_user_id=db.query(models.UserModel).filter(models.UserModel.email==current_user.email).first().id
    new_blog = models.BlogModel(title=request.title, body=request.body,author_id=current_user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return schemas.Blog.from_orm(new_blog)

# #create a blog, you must be logged in to create a blog.
# #You can use the author_id field to specify the author of the blog



#get all blogs

@router.get('/blogs', response_model=schemas.BlogListResponse, status_code=status.HTTP_200_OK)
def get_blogs(db: Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    blogs = db.query(models.BlogModel).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No blogs found')
    return schemas.BlogListResponse(message="Blogs found", data=[schemas.Blog.from_orm(blog) for blog in blogs])


#get a blog by Id

@router.get('/blog/{id}', response_model=schemas.Blog, status_code=status.HTTP_200_OK)
def get_blog_by_id(id: int, db: Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    return schemas.Blog.from_orm(blog)



#update a blog
@router.patch('/blog/{id}', response_model=schemas.Blog, status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.BlogCreate, db: Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    blog.update(dict(request))
    db.commit()
    return schemas.Blog.from_orm(blog.first())


#delete a blog

@router.delete('/blog/{id}',status_code=status.HTTP_200_OK)
def delete_blog(id: int, db: Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    db.delete(blog)
    db.commit()
    return {"message": f"Blog with id {id} deleted successfully"}