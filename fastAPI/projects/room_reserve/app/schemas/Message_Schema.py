from datetime import date
from pydantic import BaseModel, Field

from app.database import PyObjectId

class MessageToAdmin(BaseModel):
    # Populate this field with user
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    date_of_message: date = Field(default=date.today())
    message: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            PyObjectId: str
        }
        schema_extra = {
            "example": {
                "date_of_message": "2021-06-07",
                "message": "I am having trouble with the booking system"
            }
        }

