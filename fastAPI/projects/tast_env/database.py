#database.py

import motor.motor_asyncio
import motor
import beanie

from models import TaskModel


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/py_task")
    await beanie.init_beanie(
        database=client.tasks_db,
        document_models=[TaskModel],
    )

 

