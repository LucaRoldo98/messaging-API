from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from services.MessageService import MessageService
from dataClasses.MessageData import MessageData
from api.schemas.MessageSchemas import *

messageRouter = APIRouter(prefix="/messages")

@messageRouter.post("/", response_model=MessageResponseSchema, status_code=status.HTTP_201_CREATED)
async def submit_message(message: MessagePostRequestSchema, service: MessageService = Depends()):
    messageData = service.submitMessage(MessageData(**message.model_dump()))
    if messageData is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sender or recipient doesn't exist")
    return messageDataToSchema(messageData)

@messageRouter.get("/unread/{userID}", response_model=List[MessageResponseSchema])
async def get_unread_messages(userID: str, service: MessageService = Depends()):
    messages = service.getUnreadMessages(userID)
    if messages is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {userID} does not exist")
    return [messageDataToSchema(msg) for msg in messages]

@messageRouter.get("/{userID}", response_model=List[MessageResponseSchema])
async def get_messages(userID: str, startIndex: int = 0, stopIndex: int = None, service: MessageService = Depends()):
    if startIndex < 0 or stopIndex <= startIndex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Start and stop indexes must be non negative and stop index must be greater than start index.")
    messages = service.getMessages(userID, startIndex, stopIndex)
    if messages is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"UserID {userID} does not exist")
    return [messageDataToSchema(msg) for msg in messages]

@messageRouter.delete("/{messageID}", response_model=MessageDeleteResponseSchema)
async def delete_message(messageID: str, service: MessageService = Depends()):
    deletedCount = service.deleteMessage(messageID)
    if deletedCount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Message with ID {messageID} does not exist")
    return MessageDeleteResponseSchema(detail="Message deleted successfully")

@messageRouter.delete("/", response_model=MessageDeleteResponseSchema)
async def delete_messages(requestBody: MessagesDeleteRequestSchema, service: MessageService = Depends()):
    deletedCount = service.deleteMessages(requestBody.messagesID)
    if deletedCount == 0: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="None of the specified messages were found")
    return MessageDeleteResponseSchema(detail=f"{deletedCount} messages deleted successfully")
