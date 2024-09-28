from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from services.MessageService import MessageService
from dataClasses.MessageData import MessageData
from api.schemas.MessageSchemas import MessageResponseSchema, MessagePostRequestSchema, MessagesDeleteRequestSchema, DeleteResponseSchema, messageDataToSchema

messageRouter = APIRouter(prefix="/messages")

@messageRouter.post("/", response_model=MessageResponseSchema, status_code=status.HTTP_201_CREATED)
async def submit_message(message: MessagePostRequestSchema, service: MessageService = Depends()):
    messageData = service.submitMessage(MessageData(**message.model_dump()))
    return messageDataToSchema(messageData)

@messageRouter.get("/unread/{user}", response_model=List[MessageResponseSchema])
async def get_unread_messages(user: str, service: MessageService = Depends()):
    messageData = service.getUnreadMessages(user)
    return [messageDataToSchema(msg) for msg in messageData]

@messageRouter.get("/{user}", response_model=List[MessageResponseSchema])
async def get_messages(user: str, startIndex: int = 0, stopIndex: int = None, service: MessageService = Depends()):
    messages = service.getMessages(user, startIndex, stopIndex)
    return [messageDataToSchema(msg) for msg in messages]

@messageRouter.delete("/{messageID}", response_model=DeleteResponseSchema)
async def delete_message(messageID: str, service: MessageService = Depends()):
    service.deleteMessage(messageID)
    return DeleteResponseSchema(detail="Message deleted successfully")

@messageRouter.delete("/", response_model=DeleteResponseSchema)
async def delete_messages(requestBody: MessagesDeleteRequestSchema, service: MessageService = Depends()):
    service.deleteMessages(requestBody.messagesID)
    return DeleteResponseSchema(detail="Messages deleted successfully")
