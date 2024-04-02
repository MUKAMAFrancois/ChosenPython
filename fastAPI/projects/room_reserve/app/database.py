#database.py

import motor.motor_asyncio
from bson import ObjectId
from pydantic import BaseModel, Field
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import os

load_dotenv()



CONNECT_URL= os.getenv("MONGO_URL")
DB_NAME="RoomReserve"



client =motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://welldonestudy35:T1dnTl6f1RWWFi2N@cluster0.mo5bfgy.mongodb.net/RoomReserve?retryWrites=true&w=majority")

db = client[DB_NAME]


#BSON to JSON



class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return str(ObjectId(v))
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')



