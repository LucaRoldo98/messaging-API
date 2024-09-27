from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from services.MessageService import MessageService
from dataClasses.MessageData import MessageData
from api.schemas.MessageSchemas import MessageResponseSchema, MessagePostRequestSchema, MessagesDeleteRequestSchema, messageDataToSchema

messageRouter = APIRouter(prefix="/messages")

@messageRouter.post("/", response_model=MessageResponseSchema, status_code=status.HTTP_201_CREATED)
async def submit_message(message: MessagePostRequestSchema, service: MessageService = Depends()):
    try:
        messageData = service.submitMessage(MessageData(**message.model_dump()))
        return messageDataToSchema(messageData)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@messageRouter.get("/unread/{user}", response_model=List[MessageResponseSchema])
async def get_unread_messages(user: str, service: MessageService = Depends()):
    messageData = service.getUnreadMessages(user)
    return messageDataToSchema(messageData)

@messageRouter.get("/{user}", response_model=List[MessageResponseSchema])
async def get_messages(user: str, startIndex: int = 0, stopIndex: int = None, service: MessageService = Depends()):
    messages = service.getMessages(user, startIndex, stopIndex)
    if messages is None:
        raise HTTPException(status_code=404, detail="No messages found.")
    return [messageDataToSchema(msg) for msg in messages]

@messageRouter.delete("/{messageID}")
async def delete_message(messageID: str, service: MessageService = Depends()):
    service.deleteMessage(messageID)
    return {"detail": "Message deleted successfully"}

@messageRouter.delete("/")
async def delete_messages(requestBody: MessagesDeleteRequestSchema, service: MessageService = Depends()):
    if not requestBody:
        raise HTTPException(status_code=400, detail="No message IDs provided.")
    
    service.deleteMessages(requestBody.messagesID)
    return {"detail": "Messages deleted successfully"}