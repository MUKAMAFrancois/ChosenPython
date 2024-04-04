from datetime import date
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel,EmailStr,validator,HttpUrl
from fastapi import UploadFile, File






class HotelLocation(BaseModel):
    country:str
    city:str
    state:str
    street:str
    zipCode:str


class HotelPrice(BaseModel):
    perDay:float
    perWeek:float
    perMonth:float

    @validator('perDay')
    def validate_per_day(cls,perDay:float)->float:
        if perDay<=0:
            raise ValueError('Price cannot be negative')
        return perDay

    @validator('perWeek')
    def validate_per_week(cls,perWeek:float)->float:
        if perWeek<=0:
            raise ValueError('Price cannot be negative')
        return perWeek
    
    @validator('perMonth')
    def validate_per_month(cls,perMonth:float)->float:
        if perMonth<=0:
            raise ValueError('Price cannot be negative')


class HotelTestimonial(BaseModel):
    testimonial:str
    rating:int
    
    @validator('rating')
    def validate_rating(cls,rating:int)->int:
        if rating<1 or rating>5:
            raise ValueError('Rating must be between 1 and 5')
        return rating
    
    @validator('testimonial')
    def validate_testimonial(cls,testimonial:str)->str:
        if len(testimonial)<10:
            raise ValueError('Testimonial must be at least 10 characters long')
        return testimonial

class HotelFeatures(BaseModel):
    hasFreeWifi:Optional[bool] = False
    hasAirConditioning:Optional[bool] = False
    hasParking:Optional[bool] = False
    hasRestaurant:Optional[bool] = False
    offerBreakfast:Optional[bool] = False
    petsAllowed:Optional[bool] = False
    hasWaterPool:Optional[bool] = False
    nearTheCityCenter:Optional[bool] = False


class HotelCategory(str,Enum):
    one_star="1 Star"
    two_star="2 Star"
    three_star="3 Star"
    four_star="4 Star"
    five_star="5 Star"

class HotelSchema(BaseModel):
    hotelName: str
    hotelDescription: str
    hotelLocation:HotelLocation
    hotelPrice:HotelPrice
    hotelFeatures:HotelFeatures
    hotelTestimonials:Optional[List[HotelTestimonial]] = []
    isOnDiscount:Optional[bool] = False
    discountPercent:Optional[float] = 0.0
    hotelCategory:Optional[HotelCategory] = HotelCategory.one_star
    hotelImage:UploadFile = File(None)
    hotelThumbnails:Optional[List[HttpUrl]] = []


    @validator('hotelName')
    def validate_hotel_name(cls,hotelName:str)->str:
        if len(hotelName)<4:
            raise ValueError('Hotel Name must be at least 4 characters long')
        return hotelName
    
    @validator('discountPercent')
    def validate_discount_percent(cls,discountPercent:float)->float:
        if discountPercent<0 or discountPercent>100:
            raise ValueError('Discount Percent must be between 0 and 100')
        return discountPercent
    


class Hotel(HotelSchema):
    id:int
    class Config:
        orm_mode = True
        json_schema_extra={
            "example":{
                "hotelName":"Hotel ABC",
                "hotelDescription":"This is a simple hotel",
                "hotelLocation":{
                    "country":"Nepal",
                    "city":"Kathmandu",
                    "state":"Bagmati",
                    "street":"Thamel",
                    "zipCode":"44600"
                },
                "hotelPrice":{
                    "perDay":1000.0,
                    "perWeek":7000.0,
                    "perMonth":30000.0
                },
                "hotelFeatures":{
                    "hasFreeWifi":True,
                    "hasAirConditioning":True,
                    "hasParking":True,
                    "hasRestaurant":True,
                    "offerBreakfast":True,
                    "petsAllowed":True,
                    "hasWaterPool":True,
                    "nearTheCityCenter":True
                },
                "hotelTestimonials":[
                    {
                        "testimonial":"This is a great hotel",
                        "rating":5
                    }
                ],
                "isOnDiscount":True,
                "discountPercent":10.0,
                "hotelCategory":"5 Star",
                "hotelImage":"http://example.com/hotel.jpg",
                "hotelThumbnails":[
                    "http://example.com/hotel1.jpg",
                    "http://example.com/hotel2.jpg"
                ]
            }
        }


class HotelListResponse(BaseModel):
    message:str
    hotels:List[Hotel]
    