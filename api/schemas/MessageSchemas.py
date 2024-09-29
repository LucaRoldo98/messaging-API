from pydantic import BaseModel
from datetime import datetime
from typing import List
from dataClasses.MessageData import MessageData

class MessageResponseSchema(BaseModel):
    id: str
    recipientID : str
    senderID : str
    text : str
    timestamp: datetime

class MessagePostRequestSchema(BaseModel):
    recipientID : str
    senderID : str
    text : str
    
class MessagesDeleteRequestSchema(BaseModel):
    messagesID: List[str]

class MessageDeleteResponseSchema(BaseModel):
    detail : str

def messageDataToSchema(messageData: MessageData) -> MessageResponseSchema:
    return MessageResponseSchema(
            id=messageData.id,
            recipientID=messageData.recipientID,
            senderID=messageData.senderID,
            text=messageData.text,
            timestamp=messageData.timestamp,
            is_fetched=messageData.is_fetched
        )
