from datetime import date
from pydantic import BaseModel, Field

class MessageToAdmin(BaseModel):
    # Populate this field with user
    date_of_message: date = Field(default=date.today())
    message: str
