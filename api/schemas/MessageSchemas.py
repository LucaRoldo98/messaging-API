from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List
from dataClasses.MessageData import MessageData

class MessageResponseSchema(BaseModel):
    id: str
    recipient : EmailStr
    sender : EmailStr
    message : str
    timestamp: datetime

class MessagePostRequestSchema(BaseModel):
    recipient : EmailStr
    sender : EmailStr
    message : str
    
class MessagesDeleteRequestSchema(BaseModel):
    messagesID: List[str]

class DeleteResponseSchema(BaseModel):
    detail : str

def messageDataToSchema(messageData: MessageData) -> MessageResponseSchema:
    return MessageResponseSchema(
            id=messageData.id,
            recipient=messageData.recipient,
            sender=messageData.sender,
            message=messageData.message,
            timestamp=messageData.timestamp,
            is_fetched=messageData.is_fetched
        )
