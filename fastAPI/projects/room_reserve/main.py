#main.py
from fastapi import Depends, FastAPI
from app.routers import user_routes
# from app.database import MongoDBClient, connect_to_mongo, close_mongo_connection


app = FastAPI()

app.include_router(user_routes.router)



# @app.get("/connect")
# async def connect():
#     return await connect_to_mongo()

# @app.get("/close")
# async def close():
#     return await close_mongo_connection()


# @app.get("/home")
# async def home(db=Depends(MongoDBClient.get_db)):
#     return db



