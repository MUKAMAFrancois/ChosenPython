import motor.motor_asyncio
import motor
import beanie
from dotenv import load_dotenv
import os

from models.test_models import Book,User

# from models.hotel_models import HotelModel
# from models.users_models import UserLocation, UserModel

load_dotenv()


MONGO_URL = os.getenv("MONGO_URL")



async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
    await beanie.init_beanie(
        database = client.reservation,
        # document_models=[UserModel,HotelModel,UserLocation]
        document_models=[User,Book]
    )