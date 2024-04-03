
from typing import Dict, List, Optional
from datetime import date
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field, validator
from fastapi import UploadFile, File
from beanie import Document, init_beanie
from pydantic import Field








# class HotelModel(Document):
#     # hotel_name: str = Field(description="Hotel Name")
#     # hotel_location: str = Field(description="Hotel Location")
#     pass