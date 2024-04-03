from datetime import date
from hmac import new
from typing import List
from fastapi import APIRouter, HTTPException, status
from beanie import PydanticObjectId
from passlib.context import CryptContext

from models.test_models import BookInfo, User,Book
# from models.users_models import UserLocation, UserModel


user_router = APIRouter(
)



@user_router.get("/")
def testing():
    return {"message":"Hello World"}



@user_router.post("/user/register",response_model=User,status_code=201,tags=["users"])
async def register_user(request:User):
    # Check if the username or email is already taken
    username_exists = await User.find_one(User.username == request.username)
    email_exists = await User.find_one(User.email == request.email)
    if username_exists or email_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already taken"
        )
    new_user=User(
        username=request.username,
        email=request.email,
        password=request.password
    )
    await new_user.create()
    return new_user


#post a Book
@user_router.post("/post/book",response_model=Book,status_code=201,tags=["books"])
async def post_book(title: str, publication_date: date, book_creator: str):  # Remove request: Book
   book_exists = await Book.find_one(Book.title == title)  # Use title from function parameters
   if book_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Book already exists"
        )
   user = await User.find_one(User.username == book_creator)
   if not user:
       raise HTTPException(
          status_code=404,
            detail="Author not found. You must register for to be an author"
       )
   
   new_book=Book(
        title=title,  # Use title from function parameters
        publication_date=publication_date,  # Use publication_date from function parameters
        author=user.link() # Create a Link to the User object
    )
   await new_book.create()
   book_info = BookInfo(book_id=new_book.id, title=title, publication_date=publication_date)
   user.books_written.append(book_info)  # Append the BookInfo instance
   await user.save()

   return new_book

#Get all Books
@user_router.get("/books",response_model=List[Book],tags=["books"],status_code=200)
async def get_all_books():
    books = await Book.all().to_list()
    return books

#Get all Users

@user_router.get("/users",response_model=List[User],tags=["users"],status_code=200)
async def get_all_users():
    users = await User.all().to_list()
    return users

# #register user
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# @user_router.post("/register",response_model=UserModel,status_code=201)
# async def register_user(request:UserModel):
#     # Check if the username or email is already taken
#     username_exists = await UserModel.find_one(UserModel.username == request.username)
#     email_exists = await UserModel.find_one(UserModel.email == request.email)
#     if username_exists or email_exists:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="Username or email already taken"
#         )
   
#     #Create User Location
#     user_location=await UserLocation.create(
#         city=request.user_location.city,
#         state=request.user_location.state,
#         country=request.user_location.country,
#         user=new_user.id 
#     )
    
#     new_user=UserModel(
#         username=request.username,
#         email=request.email,
#         password=pwd_context.hash(request.password),
#         phone_number=request.phone_number,
#         userRole=request.userRole,
#         user_location=user_location  
#     )

#     await new_user.create()
#     return new_user

