#hotel Model

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean,Float
from sqlalchemy.orm import relationship
from config.database import Base



class HotelModel(Base):
    __tablename__='hotels'
    id=Column(Integer,primary_key=True,index=True)
    hotelName=Column(String(100))
    hotelDescription=Column(String)
    hotelLocation=Column(String)
    hotelPrice=Column(Float)
    hotelFeatures=Column(String)
    hotelTestimonials=Column(String)
    isBooked=Column(Boolean,default=False)
    gotSubscription=Column(Boolean,default=False)
    isOnDiscount=Column(Boolean)
    discountPercent=Column(Float)
    hotelCategory=Column(String)
    hotelImage=Column(String)
    hotelThumbnails=Column(String)
    user_id=Column(Integer,ForeignKey('users.id'))
    user=relationship('UserModel',back_populates='hotelsBooked')
    subscribers = relationship('SubscribeModel',back_populates='toWhichHotel')