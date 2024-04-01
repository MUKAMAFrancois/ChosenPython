#user_schemas.py
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field

from app.database import PythonObjectEncoder



class UserSchema(BaseModel):
    id:PythonObjectEncoder=Field(default_factory=PythonObjectEncoder,alias="_id")
    username:str = Field(...)
    email:EmailStr = Field(...)
    password:str = Field(...)

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