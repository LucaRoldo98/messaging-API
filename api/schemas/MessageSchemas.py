from pydantic import BaseModel
from datetime import datetime
from typing import List

class MessageSchema(BaseModel):
    recipient : str
    sender : str
    message : str

class MessagePostRequestSchema(BaseModel):
    recipient : str
    sender : str
    message : str
    
class MessagesDeleteRequestSchema(BaseModel):
    messagesID: List[str]

