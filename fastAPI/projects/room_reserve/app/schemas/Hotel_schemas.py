#Hotel_schemas.py

from typing import Dict, List, Optional
from datetime import date
from bson import ObjectId
from pydantic import BaseModel, Field, validator
from fastapi import UploadFile


class HotelLocation(BaseModel):
    hotel_id: ObjectId  # Reference to the hotel
    city: str
    state: str
    country: str

class HotelPrice(BaseModel):
    hotel_id: ObjectId  # Reference to the hotel
    perday_price:float
    perweek_price:float
    permonth_price:float

    #must be linked with specific hotel

class HotelTestimonials(BaseModel):
    hotel_id: ObjectId  # Reference to the hotel
    witnessed_by: ObjectId  # Reference to the user
    message:str

class HotelFeatures(BaseModel):
    hotel_id: ObjectId  # Reference to the hotel
    has_free_wifi:bool
    has_air_conditioning:bool
    has_parking:bool
    has_restaurant:bool
    offer_breakfast:bool
    pets_allowed:bool
    near_the_city_center:bool
    has_water_pool:bool

class HotelSchema(BaseModel):
    id:Optional[ObjectId]=Field(default_factory=ObjectId,alias="_id")
    hotel_name:str = Field(..., description="Name of the hotel")
    hotel_location:HotelLocation = Field(..., description="Location of the hotel")
    hotel_description:str = Field(..., description="Description of the hotel")
    hotel_image_url: str=Field(..., description="Image URL of the hotel")
    is_onDiscount:Optional[bool] = Field(default=False)
    discount_percent=Optional[int] = Field(default=0)
    hotel_price:HotelPrice = Field(..., description="Price of the hotel")
    hotel_category:str = Field(..., description="Category of the hotel '5-star', '4-star', '3-star', '2-star', '1-star'")
    number_of_rooms:int = Field(..., description="Number of rooms in the hotel")
    thumnails:List[str] =[Field(...,description="Thumbnails of the hotel")]
    testimonials:List[HotelTestimonials] = [Field(...,description="Testimonials of the hotel")]
    hotel_features:HotelFeatures
    
    @validator('hotel_price')
    def hotel_price_must_be_positive(cls,v):
        if v<0:
            raise ValueError("Hotel price must be positive")
        return v
    
    @validator('hotel_rating')
    def hotel_rating_must_be_between_0_and_5(cls,v):
        if v<0 or v>5:
            raise ValueError("Hotel rating must be between 0 and 5")
        return v
    
    @validator('discount_percent')
    def discount_percent_must_be_between_0_and_100(cls, v):
        if v < 0 or v > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        return v


    @validator('number_of_rooms')
    def number_of_rooms_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Number of rooms must be a positive integer")
        return v