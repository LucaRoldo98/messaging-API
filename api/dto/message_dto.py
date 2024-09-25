from datetime import datetime
from pydantic import BaseModel, EmailStr

class MessageDTO(BaseModel):
    def __init__(self, sender: EmailStr, recipient: EmailStr, message: str, timestamp: datetime):
        self.recipient = recipient
        self.sender = sender
        self.message = message
        self.timestamp = timestamp
