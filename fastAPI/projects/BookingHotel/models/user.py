#user Models

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from config.database import Base
from models.Message import MessageModel
from models.hotel import HotelModel # so needed in order to establish relationship




class UserModel(Base):
    __tablename__ ='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True)
    email=Column(String(100),unique=True)
    password=Column(String(100))
    phoneNumber=Column(String(15))
    userRole=Column(String(10))
    profilePic=Column(String)
    hasBookedHotel=Column(Boolean,default=False)
    startingDateOfStay=Column(Date)
    endingDateOfStay=Column(Date)
    numberOfPeopleToBookWith=Column(Integer,default=1)
    hotelsBooked=relationship('HotelModel',back_populates='user')
    location=relationship('LocationModel',back_populates='user')
    messages=relationship('MessageModel',back_populates='user')
    location_id = Column(Integer, ForeignKey('locations.id'))


class LocationModel(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String)
    city = Column(String)
    state = Column(String)
    street = Column(String)
    zipCode = Column(String)
    user=relationship('UserModel',back_populates='location')
    