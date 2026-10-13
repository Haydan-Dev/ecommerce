from sqlalchemy import Column,Integer,String,Boolean,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime as dt
from app.db.db import Base

class User(Base):   
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(125))
    email = Column(String(225),unique=True,index=True)
    hashed_password = Column(String(255))
    phone_number = Column(String(15))
    is_verified = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=dt.utcnow)
    role = Column(String(20),default="Customer")

    orders = relationship("Order", back_populates="owner")
