#user schemas

from datetime import date
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel,EmailStr,validator

from schemas.hotel import Hotel







class UserRole(str,Enum):
    user="user"
    admin="admin"

class UserLocation(BaseModel):
    country: str
    city: str
    state: str
    street: str
    zipCode: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    phoneNumber: str
    userRole: UserRole
    hasSubscribed: Optional[bool] = False
    profilePic: Optional[str] = None
    hasBookedHotel: Optional[bool] = False
    location:UserLocation
    startingDateOfStay: Optional[date] = None
    endingDateOfStay: Optional[date] = None
    numberOfPeopleToBookWith: Optional[int] = 1
    hotelsBooked: Optional[List[Hotel]] = []


    @validator('password')
    def validate_password_strength(cls,password:str)->str:
        special_characters='!@#$%^&*()-+'
        if len(password)<8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in password):
            raise ValueError('Password must contain a number')
        if not any(char.isupper() for char in password):
            raise ValueError('Password must contain an uppercase letter')
        if not any(char.islower() for char in password):
            raise ValueError('Password must contain a lowercase letter')
        if not any(char in special_characters for char in password):
            raise ValueError('Password must contain a special character')
        return password
    
    @validator('username')
    def validate_username(cls,username:str)->str:
        if len(username)<4:
            raise ValueError('Username must be at least 4 characters long')
        return username
    
    @validator('email')
    def validate_email(cls,email:EmailStr)->EmailStr:
        symbols=['@','.']
        if email.split('@')[1]=='':
            raise ValueError('Invalid email')
        if not any(char in symbols for char in email):
            raise ValueError('Invalid email')
        return email
    





class User(UserSchema):
    id: Optional[int]

    class Config:
        from_attributes = True
        orm_mode = True
        populate_by_name = True

        json_schema_extra = {
                "example": {
                    "username": "john_doe",
                    "email": "john@gmail.com",
                    "password": "John@123",
                    "phoneNumber": "+123456789",
                    "userRole": "user",
                    "profilePic": "profile.jpg",
                    "hasBookedHotel": False,
                    "location": {
                        "country": "USA",
                        "city": "New York",
                        "state": "New York",
                        "street": "123 Main Street",
                        "zipCode": "12345"
                    },
                    "startingDateOfStay": "2022-01-01",
                    "endingDateOfStay": "2022-01-15",
                    "numberOfPeopleToBookWith": 2,
                    "hotelsBooked": [
                        {
                            "hotelName": "Hotel ABC",
                            "hotelDescription": "This is a simple hotel",
                            "hotelLocation": {
                                "country": "Nepal",
                                "city": "Kathmandu",
                                "state": "Bagmati",
                                "street": "Thamel",
                                "zipCode": "44600"
                            },
                            "hotelPrice": {
                                "perDay": 1000.0,
                                "perWeek": 7000.0,
                                "perMonth": 30000.0
                            },
                            "hotelFeatures": {
                                "hasFreeWifi": True,
                                "hasAirConditioning": True,
                                "hasParking": True,
                                "hasRestaurant": True,
                                "offerBreakfast": True,
                                "petsAllowed": True,
                                "hasWaterPool": True,
                                "nearTheCityCenter": True
                            },
                            "hotelTestimonials": [
                                {
                                    "testimonial": "This is a great hotel",
                                    "rating": 5
                                }
                            ],
                            "isOnDiscount": True,
                            "discountPercent": 10.0,
                            "hotelCategory": "5 Star",
                            "hotelImage": "http://example.com/hotel.jpg",
                            "hotelThumbnails": [
                                "http://example.com/hotel1.jpg",
                                "http://example.com/hotel2.jpg"
                            ]
                        }
                    ]
                }
            }


class UserListResponse(BaseModel):
    message:str
    users:List[User]