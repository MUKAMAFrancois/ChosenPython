#schemas.py

from typing import List
from pydantic import BaseModel,validator,EmailStr,constr






class BlogCreate(BaseModel):
    title:str
    body:str
    # author_id:int

    @validator('title')
    def validate_title(cls,title:str)->str:
        if len(title)<4:
            raise ValueError('Title must be at least 4 characters long')
        return title
    
    @validator('body')
    def validate_body(cls,body:str)->str:
        if len(body)<4:
            raise ValueError('Body must be at least 4 characters long')
        return body
    
    # @validator('author_id')
    # def validate_author_id(cls,author_id:int)->int:
    #     if author_id<1:
    #         raise ValueError('Invalid author id')
    #     return author_id
    
    
class Blog(BlogCreate):
    id:int
    class Config:
      
        from_attributes=True
        # orm_mode=True


class BlogListResponse(BaseModel):
    message: str
    data: List[Blog]

    






# class UserCreate(BaseModel):
#     email:EmailStr
#     username:str 
#     password:str 


#     @validator('password')
#     def validate_password_strength(cls,password:str)->str:
#         special_characters='!@#$%^&*()-+'
#         if len(password)<8:
#             raise ValueError('Password must be at least 8 characters long')
#         if not any(char.isdigit() for char in password):
#             raise ValueError('Password must contain a number')
#         if not any(char.isupper() for char in password):
#             raise ValueError('Password must contain an uppercase letter')
#         if not any(char.islower() for char in password):
#             raise ValueError('Password must contain a lowercase letter')
#         if not any(char in special_characters for char in password):
#             raise ValueError('Password must contain a special character')
#         return password
    
#     @validator('username')
#     def validate_username(cls,username:str)->str:
#         if len(username)<4:
#             raise ValueError('Username must be at least 4 characters long')
#         return username
    
#     @validator('email')
#     def validate_email(cls,email:EmailStr)->EmailStr:
#         symbols=['@','.']
#         if email.split('@')[1]=='':
#             raise ValueError('Invalid email')
#         if not any(char in symbols for char in email):
#             raise ValueError('Invalid email')
#         return email
    

# class User(UserCreate):
#     id:int

#     class Config:
#         orm_mode=True