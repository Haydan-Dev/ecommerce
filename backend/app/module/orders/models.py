from sqlalchemy import Integer,String,ForeignKey,Float,Column,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime as dt
from app.db.db import Base

class Order(Base): 
    __tablename__="orders"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    total_amount=Column(Float)
    status=Column(String(55),default="pending")
    created_at=Column(DateTime,default=dt.utcnow)
    owner=relationship("User", back_populates="orders")

class OrderItem(Base):
    __tablename__ = "order_items"
    id=Column(Integer,primary_key=True,index=True)
    order_id=Column(Integer,ForeignKey("orders.id"))
    product_id=Column(Integer,ForeignKey("products.id"))
    quantity=Column(Integer,default=1)
    price=Column(Float)
    created_at=Column(DateTime,default=dt.utcnow)
    