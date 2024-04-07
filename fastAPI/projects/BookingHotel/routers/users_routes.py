from datetime import date
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from config.database import get_db
from schemas.users import UserSchema,User
from models.user import UserModel,LocationModel


userRouter=APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)




@userRouter.get("/")
def test():
    return {"message":"Hello World"}


#register a user
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

@userRouter.post("/register", response_model=User, status_code=201, description="Register a user")
def register_user(user_data: UserSchema, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user_data.password)

    location = LocationModel(
        country=user_data.country,
        city=user_data.city,
        state=user_data.state,
        street=user_data.street,
        zipCode=user_data.zipCode
    )
    db.add(location)
    db.commit()
    db.refresh(location)

    newUser = UserModel(
        username=user_data.username,
        email=user_data.email,
        password=hashed_password,
        phoneNumber=user_data.phoneNumber,
        userRole=user_data.userRole,
        profilePic=user_data.profilePic,
        hasBookedHotel=user_data.hasBookedHotel,
        startingDateOfStay=user_data.startingDateOfStay,
        endingDateOfStay=user_data.endingDateOfStay,
        numberOfPeopleToBookWith=user_data.numberOfPeopleToBookWith,
        location_id=location.id
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return User.from_orm(newUser)