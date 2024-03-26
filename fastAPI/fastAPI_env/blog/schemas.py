from pydantic import BaseModel



class Blog(BaseModel):
    title: str
    body: str
    user_id: int

    class Config:
        orm_mode = True