from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from services.MessageService import MessageService
from dataClasses.MessageData import MessageData
from api.schemas.MessageSchemas import MessageResponseSchema, MessagePostRequestSchema, MessagesDeleteRequestSchema, MessagesDeleteResponseSchema, messageDataToSchema

messageRouter = APIRouter(prefix="/messages")

@messageRouter.post("/", response_model=MessageResponseSchema, status_code=status.HTTP_201_CREATED)
async def submit_message(message: MessagePostRequestSchema, service: MessageService = Depends()):
    messageData = service.submitMessage(MessageData(**message.model_dump()))
    return messageDataToSchema(messageData)

@messageRouter.get("/unread/{user}", response_model=List[MessageResponseSchema])
async def get_unread_messages(user: str, service: MessageService = Depends()):
    messages = service.getUnreadMessages(user)
    if messages is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user} does not exist")
    return [messageDataToSchema(msg) for msg in messages]

@messageRouter.get("/{user}", response_model=List[MessageResponseSchema])
async def get_messages(user: str, startIndex: int = 0, stopIndex: int = None, service: MessageService = Depends()):
    messages = service.getMessages(user, startIndex, stopIndex)
    if messages is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user} does not exist")
    return [messageDataToSchema(msg) for msg in messages]

@messageRouter.delete("/{messageID}", response_model=MessagesDeleteResponseSchema)
async def delete_message(messageID: str, service: MessageService = Depends()):
    deletedCount = service.deleteMessage(messageID)
    if deletedCount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Message with ID {messageID} does not exist")
    return MessagesDeleteResponseSchema(detail="Message deleted successfully")

@messageRouter.delete("/", response_model=MessagesDeleteResponseSchema)
async def delete_messages(requestBody: MessagesDeleteRequestSchema, service: MessageService = Depends()):
    deletedCount = service.deleteMessages(requestBody.messagesID)
    if deletedCount == 0: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No messages with specified IDs found")
    return MessagesDeleteResponseSchema(detail=f"{deletedCount} messages deleted successfully")
