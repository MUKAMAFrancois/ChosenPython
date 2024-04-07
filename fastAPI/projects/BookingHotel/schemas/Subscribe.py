#subscribe schema

from pydantic import BaseModel, EmailStr




class SubscribeSchema(BaseModel):
    email: EmailStr

