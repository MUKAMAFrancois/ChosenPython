#models.py

from datetime import datetime
from beanie import Document, init_beanie
from pydantic import Field



class TaskModel(Document):
    title: str = Field(max_length=200)
    completed: bool = False
    date_created:datetime = datetime.now()

    class Settings:
        name="task_db"

    class Config:
        schema_extra={
            "title":"Task title",
            "completed":False,
            "date_created":datetime.now()
        }