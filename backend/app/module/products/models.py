from sqlalchemy import Column,Integer,Boolean,String,DateTime,Float,ForeignKey
from datetime import datetime as dt
from app.db.db import Base 

class Category(Base):
    __tablename__="categories"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(225)) 
    description=Column(String(225))

class Product(Base): 
    __tablename__ = "products"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(125))
    description = Column(String(255))
    price = Column(Float)
    discount_percentage = Column(Float)
    image_url = Column(String(555))
    stock = Column(Integer,default=0)
    category_id = Column(Integer,ForeignKey("categories.id"))
    is_active = Column(Boolean,default=False)
    created_at = Column(DateTime,default=dt.utcnow)
    updated_at = Column(DateTime,default=dt.utcnow,onupdate=dt.utcnow)

