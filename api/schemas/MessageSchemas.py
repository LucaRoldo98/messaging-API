from pydantic import BaseModel
from datetime import datetime
from typing import List
from dataClasses.MessageData import MessageData

class MessageResponseSchema(BaseModel):
    id: str
    recipient : str
    sender : str
    message : str
    timestamp: datetime

class MessagePostRequestSchema(BaseModel):
    recipient : str
    sender : str
    message : str
    
class MessagesDeleteRequestSchema(BaseModel):
    messagesID: List[str]

def messageDataToSchema(messageData: MessageData) -> MessageResponseSchema:
    return MessageResponseSchema(
            id=messageData.id,
            recipient=messageData.recipient,
            sender=messageData.sender,
            message=messageData.message,
            timestamp=messageData.timestamp,
            is_fetched=messageData.is_fetched
        )
