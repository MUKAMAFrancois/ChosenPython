from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from passlib.context import CryptContext


from blog import models,schemas
from blog.database import get_db


router=APIRouter(
    tags=["users"]
)



#register user
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#register user
@router.post("/register", response_model=schemas.User, status_code=status.HTTP_201_CREATED,tags=["users"])
def register_user(request:schemas.UserCreate,db:Session=Depends(get_db)):
    hashed_password=pwd_context.hash(request.password)
    new_user=models.UserModel(username=request.username,
                              email=request.email,
                              password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return schemas.User.from_orm(new_user)




#login a user



#show all users
@router.get('/users',response_model=schemas.UserListResponse,status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    users=db.query(models.UserModel).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No Users found')
    return schemas.UserListResponse(message="Users found", data=[schemas.User.from_orm(user) for user in users])


#get user by Id

@router.get('/user/{id}', response_model=schemas.User, status_code=status.HTTP_200_OK)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return schemas.User.from_orm(user)


#update user details

# @router.patch('/user/update/{id}', response_model=schemas.User, status_code=status.HTTP_202_ACCEPTED)
# def update_user(id: int, request: schemas.UserCreate, db: Session = Depends(get_db)):
#     user = db.query(models.UserModel).filter(models.UserModel.id == id)
#     if not user.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
#     user.update(dict(request))
#     db.commit()
#     return schemas.User.from_orm(user.first())


#delete a user
@router.delete('/user/delete/{id}',status_code=status.HTTP_200_OK)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    db.delete(user)
    db.commit()
    return {"message": f"User with id {id} deleted successfully"}




