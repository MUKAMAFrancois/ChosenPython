from pydantic import BaseModel, EmailStr, Field

class SubscribeToNews(BaseModel):
    email: EmailStr = Field(..., description="Email address to subscribe to news updates")
   
    class Config:
        schema_extra = {
            "example": {
                "email": "example@example.com"
            }
        }
