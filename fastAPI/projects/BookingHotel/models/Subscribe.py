from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from models.hotel import HotelModel



class SubscribeModel(Base):
    __tablename__ ="subscribers"

    email = Column(String(255))
    toWhichHotel=relationship('HotelModel',back_populates='subscribers')