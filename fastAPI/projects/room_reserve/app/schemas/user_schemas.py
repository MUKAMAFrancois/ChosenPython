#user_schemas.py
from typing import Dict, List, Optional
from datetime import date
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field, validator
from fastapi import UploadFile

from app.database import PyObjectId



class UserLocation(BaseModel):
    user_id: ObjectId  # Reference to the user
    city: str
    state: str
    country: str

class UserSchema(BaseModel):
    id:PyObjectId=Field(default_factory=PyObjectId,alias="_id")
    username:str = Field(...)
    email:EmailStr = Field(...)
    password:str = Field(...)
    phone_number:str = Field(...)
    userRole:str = Field(...)
    profile_picture: Optional[UploadFile] = None
    is_active:Optional[bool] = Field(default=True)
    user_location:UserLocation = Field(...)
    has_booked_hotel:Optional[bool] = Field(default=False)
    starting_date_of_booking: Optional[date] = Field(...)
    ending_date_of_booking: Optional[date] = Field(...)
    number_of_people_for_hotel:Optional[int] = Field(...)
    hotels_booked:Optional[List[ObjectId]] = Field(default_factory=list)


    @validator("phone_number")
    def phone_number_must_contain_11_digits(cls,v):
        if len(v)!=11:
            raise ValueError("Phone number must contain 11 digits")
        return v
    
    @validator("userRole")
    def user_role_must_be_valid(cls,v):
        if v not in ["admin","user"]:
            raise ValueError("User role must be either admin or user")
        return v
    
    @validator('password')
    def validate_password_strength(cls,password:str)->str:
        special_characters='!@#$%^&*()-+'
        if len(password)<8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in password):
            raise ValueError('Password must contain a number')
        if not any(char.isupper() for char in password):
            raise ValueError('Password must contain an uppercase letter')
        if not any(char.islower() for char in password):
            raise ValueError('Password must contain a lowercase letter')
        if not any(char in special_characters for char in password):
            raise ValueError('Password must contain a special character')
        return password
    
    @validator('username')
    def validate_username(cls,username:str)->str:
        if len(username)<4:
            raise ValueError('Username must be at least 4 characters long')
        return username
    
    @validator('email')
    def validate_email(cls,email:str)->EmailStr:
       symbols=['@','.']
       if email.split('@')[1].split('.')[0]=="":
           raise ValueError('Invalid email')
       
       if not any(char in symbols for char in email):
           raise ValueError('Invalid email')
       return email


    class Config:
        allowed_population_field_name=True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId:str
        }

        schema_extra = {
            "example":{
                "username":"John",
                "email":"john@gmail.com",
                "password":"password"
            }
        }