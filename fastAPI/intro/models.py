#models.py
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Gender(str, Enum):
    male="Male"
    female ="Female"

class UserRole(str, Enum):
    admin="Admin"
    user="User"
    student="Student"

class Region (str, Enum):
    north="North"
    south="South"
    east="East"
    west="West"
    central="Central"
    north_east="North East"

class User (BaseModel):
    id:Optional[UUID] = uuid4()
    first_name:str
    last_name:str
    middle_name:Optional[str] = None
    telephone_number:str
    gender:Gender 
    userRole:UserRole
    location:List[Region]