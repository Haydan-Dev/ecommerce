from pydantic import BaseModel # for basemodel 
from pydantic import EmailStr # for email validation
from pydantic import Field    # for password validation
from datetime import datetime as dt

class Users:
    @staticmethod
    def create_users(BaseModel):
            id:int
            name:str
            email:EmailStr
            hashed_password:Field
            phone_number:str
            is_verified:bool
            id_active:bool
            created_at: dt.utcnow