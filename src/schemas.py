from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class ImageOut(BaseModel):
    id: int
    filename: str
    upload_date: datetime
    extracted_text: str

    class Config:
        from_attributes = True