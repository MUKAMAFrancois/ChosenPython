#main.py
from fastapi import Depends, FastAPI
from app.database import MongoDBClient, connect_to_mongo, close_mongo_connection


app = FastAPI()

# @app.get("/connect")
# async def connect():
#     return await connect_to_mongo()

# @app.get("/close")
# async def close():
#     return await close_mongo_connection()


@app.get("/home")
async def home(db=Depends(MongoDBClient.get_db)):
    return db




from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://welldonestudy35:T1dnTl6f1RWWFi2N@cluster0.mo5bfgy.mongodb.net/ROOMRESERVE?retryWrites=true&w=majority&appName=Cluster0"


# Create a new client and connect to the server
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)