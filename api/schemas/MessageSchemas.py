from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List

class MessageSchema(BaseModel):
    id : str
    recipient : EmailStr
    sender : EmailStr
    message : str
    timestamp : datetime

class MessagePostRequestSchema(BaseModel):
    recipient : EmailStr
    sender : EmailStr
    message : str
    
class MessagesDeleteRequestSchema(BaseModel):
    messagesID: List[str]

