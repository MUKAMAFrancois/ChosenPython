from typing import Dict, List
from datetime import date
from typing import Any, Optional
from beanie import Document, PydanticObjectId,Link
from bson import ObjectId
from pydantic import BaseModel, Field


class BookInfo(BaseModel):
    book_id: PydanticObjectId
    title: str
    publication_date: date

class User(Document):
    id: Optional[PydanticObjectId] = Field(default_factory=PydanticObjectId, alias="_id")
    username: str
    email: str
    password: str
    books_written: List[BookInfo] = []

    class Settings:
        name = "users"  
    
    class Config:
        populate_by_name = True
        json_schema_extra={
            "example":{
                "username":"John Doe",
                "email":"john@gmail.com",
                "password":"password"
            }
        }

    def link(self) -> Link["User"]:
        return Link(self, document_class=User)



class Book(Document):
    id: Optional[PydanticObjectId] = Field(default_factory=PydanticObjectId, alias="_id")
    title: str
    publication_date: date
    author: Link[User]

    class Settings:
        name = "books"
    
    class Config:
        populate_by_name = True
        json_schema_extra={
            "example":{
                "title":"The Alchemist",
                "publication_date":"1988-01-01"
            }
        }

    def link(self) -> Link["Book"]:
        return Link(self, document_class=Book)