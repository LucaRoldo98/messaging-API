from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from services.MessageService import MessageService
from dataClasses.MessageData import MessageData
from api.schemas.MessageSchemas import MessageSchema, MessagePostRequestSchema, MessagesDeleteRequestSchema, messageDataToSchema

messageRouter = APIRouter(prefix="/messages")

@messageRouter.post("/", response_model=MessageSchema, status_code=status.HTTP_201_CREATED)
async def submit_message(message: MessagePostRequestSchema, service: MessageService = Depends()):
    try:
        message_data = service.submitMessage(MessageData(**message.model_dump()))
        return messageDataToSchema(message_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@messageRouter.get("/unread/{user}", response_model=List[MessageSchema])
async def get_unread_messages(user: str, service: MessageService = Depends()):
    return service.getUnreadMessages(user)

@messageRouter.get("/{user}", response_model=List[MessageSchema])
async def get_messages(user: str, startIndex: int = 0, stopIndex: int = None, service: MessageService = Depends()):
    messages = service.getMessages(user, startIndex, stopIndex)
    if messages is None:
        raise HTTPException(status_code=404, detail="No messages found.")
    return messages

@messageRouter.delete("/{messageID}")
async def delete_message(messageID: str, service: MessageService = Depends()):
    result = service.deleteMessage(messageID)
    if not result:
        raise HTTPException(status_code=404, detail="Message not found.")
    return {"detail": "Message deleted successfully"}

@messageRouter.delete("/")
async def delete_messages(messagesID: MessagesDeleteRequestSchema, service: MessageService = Depends()):
    if not messagesID:
        raise HTTPException(status_code=400, detail="No message IDs provided.")
    
    service.deleteMessages(messagesID)
    return {"detail": "Messages deleted successfully"}