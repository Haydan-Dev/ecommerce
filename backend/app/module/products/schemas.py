from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from datetime import datetime as dt 

class Products:
    @staticmethod
    def Create_products(Basemodel):
        id:int
        Name:str 
        description:str
        price:float
        discount_percentage:float
        image_url:str
        stock:int
        category_id:int
        is_active:bool
        created_at:bool
        updated_at:dt.utcnow
