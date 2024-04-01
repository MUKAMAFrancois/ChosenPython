#database.py

from typing import Optional
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import os

load_dotenv()



CONNECT_URL= os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")


class MongoDBClient:
    client:Optional[MongoClient] = None


    @classmethod
    async def get_client(cls) -> MongoClient:
        if cls.client is None:
            try:
                cls.client = MongoClient(CONNECT_URL)
            except ConnectionFailure:
                print("Server not available")
        return cls.client
    
    @classmethod
    async def get_db(cls) -> MongoClient:
        client=await cls.get_client()
        return client[DB_NAME]
    

async def connect_to_mongo():
    client=await MongoDBClient.get_client()
    return client


async def close_mongo_connection():
    client=await MongoDBClient.get_client()
    client.close()
    print("Connection closed")