from pydantic import BaseModel
from datetime import datetime
from typing import List
from dataClasses.MessageData import MessageData

class MessageResponseSchema(BaseModel):
    id: str
    recipient : str
    sender : str
    text : str
    timestamp: datetime

class MessagePostRequestSchema(BaseModel):
    recipient : str
    sender : str
    text : str
    
class MessagesDeleteRequestSchema(BaseModel):
    messagesID: List[str]

class MessageDeleteResponseSchema(BaseModel):
    detail : str

def messageDataToSchema(messageData: MessageData) -> MessageResponseSchema:
    return MessageResponseSchema(
            id=messageData.id,
            recipient=messageData.recipient,
            sender=messageData.sender,
            text=messageData.text,
            timestamp=messageData.timestamp,
            is_fetched=messageData.is_fetched
        )
