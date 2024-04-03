#users_models.py












# from typing import Dict, List, Optional,Any
# from datetime import date
# from bson import ObjectId
# from pydantic import BaseModel, EmailStr, Field, validator,Field,schema
# from fastapi import UploadFile
# from beanie import Document,Link



# class PyObjectId(str):
#     @classmethod
#     def __get_validators__(cls) -> Any:
#         yield cls.validate

#     @classmethod
#     def validate(cls, v: Any) -> ObjectId:
#         if not ObjectId.is_valid(v):
#             raise ValueError('Invalid ObjectId')
#         return ObjectId(v)
#     class Config:
#         json_schema_extra = None


# class UserLocation(Document):
#     user:PyObjectId = Field(...,description="User") # Link UserLocation to UserModel
#     city: str
#     state: str
#     country: str
    
#     class Settings:
#         name="user_locations_db"

#     class Config:
#         arbitrary_types_allowed = True
#         schema_extra={
#             "example":{
#                 "city":"Delhi",
#                 "state":"Delhi",
#                 "country":"India"
#             }
#         }

# class UserModel(Document):
#     username:str = Field(...,max_length=50,description="Username")
#     email: EmailStr = Field(...,description="Email")
#     password: str = Field(...,description="Password")
#     phone_number: str = Field(...,description="Phone Number", max_length=15)
#     userRole: str = Field(description="User Role", max_length=10,default="user")
#     profile_picture: Optional[UploadFile] =None
#     is_active: bool = Field(default=True, description="Is Active")
#     user_location: PyObjectId = Field(...,description="User Location") # Link UserModel to UserLocation
#     has_booked_hotel: Optional[bool] = Field(default=False, description="Has Booked Hotel")
#     starting_date_of_booking: Optional[date] = Field(...,description="Starting Date of Booking")
#     ending_date_of_booking: Optional[date] = Field(...,description="Ending Date of Booking")
#     number_of_people_you_are_with: Optional[int] = Field(...,description="Number of People you are with")
#     hotels_booked: Optional[List[PyObjectId]] = Field(...,description="Hotels Booked")

#     @validator("userRole")
#     def user_role_must_be_valid(cls,v):
#         if v not in ["admin","user"]:
#             raise ValueError("User role must be either admin or user")
#         return v
    
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
    
#     @validator('email')
#     def validate_email(cls,email:str)->EmailStr:
#        symbols=['@','.']
#        if email.split('@')[1].split('.')[0]=="":
#            raise ValueError('Invalid email')
       
#        if not any(char in symbols for char in email):
#            raise ValueError('Invalid email')
#        return email
    


#     class Settings:
#         name="users_db"

#     class Config:
#         arbitrary_types_allowed = True
#         schema_extra={
#             "example":{
#                 "username":"john",
#                 "email":"john@gmail.com",
#                 "password":"John@123",
#                 "phone_number":"1234567890",
#                 "userRole":"user",
#                 "profile_picture":None,
#                 "is_active":True,
#                 "user_location":{
#                     "city":"Delhi",
#                     "state":"Delhi",
#                     "country":"India"
#                 },
#                 "has_booked_hotel":False,
#                 "starting_date_of_booking":None,
#                 "ending_date_of_booking":None,
#                 "number_of_people_you_are_with":None,
#                 "hotels_booked":[]
#             }
#         }


