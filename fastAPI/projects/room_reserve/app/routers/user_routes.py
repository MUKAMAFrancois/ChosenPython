#user_routes.py
from fastapi import APIRouter,Depends,HTTPException,status
from passlib.context import CryptContext
from app.schemas import user_schemas
from fastapi.encoders import jsonable_encoder
from app.database import db



router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/test")
def test():
    return {"message":"Hello World"}

#register user
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
@router.post("/register", description="Register a new user",status_code=status.HTTP_201_CREATED)
async def register_user(user_info:user_schemas.UserSchema):
   user_info=jsonable_encoder(user_info)

   #check for duplicates
   username_found=db.users.find_one({"username":user_info["username"]})
   email_found=db.users.find_one({"email":user_info["email"]})
   if username_found:
         raise HTTPException(status_code=409,detail="Username already taken")
   if email_found:
        raise HTTPException(status_code=409,detail="Email already taken")
   
    #hash password
   user_info["password"]=pwd_context.hash(user_info["password"])
   db.users.insert_one(user_info)
   return {"message":"User registered successfully", "data":user_info}
