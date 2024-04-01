#database.py

import motor.motor_asyncio
from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import os

load_dotenv()



CONNECT_URL= os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

client =motor.motor_asyncio.AsyncIOMotorClient(CONNECT_URL)

db = client[DB_NAME]


#BSON to JSON



class PythonObjectEncoder(ObjectId):

    @classmethod
    def get_validators(cls):
        yield cls.validate


    @classmethod
    def validate(cls,v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)
    
    @classmethod
    def modify_schema(cls,field_schema):
        field_schema.update(type='string')
        return field_schema

    



