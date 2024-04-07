from datetime import date
from typing import Optional
from pydantic import BaseModel,validator







class SendMessageSchema(BaseModel):
    dateOfSending:date =date.today()
    messge:Optional[str] = None

    @validator('message')
    def validate_message(cls,message:str)->str:
        if len(message) <=10:
            raise ValueError("Message must be atleast 10 characters long")
        return message