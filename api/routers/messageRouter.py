from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from services.MessageService import MessageService
from dataClasses.MessageData import MessageData

messageRouter = APIRouter(prefix="/messages")

@messageRouter.post("/messages/", response_model=MessageData)
async def submit_message(message: MessageData, service: MessageService = Depends()):
    try:
        return service.submitMessage(message)
    except ValueError as es:
        raise HTTPException(status_code=400, detail=str(e))

@messageRouter.get("/messages/unread/{user}", response_model=List[MessageData])
async def get_unread_messages(user: str, service: MessageService = Depends()):
    return service.getUnreadMessages(user)

@messageRouter.get("/messages/{user}", response_model=List[MessageData])
async def get_messages(user: str, startIndex: int = 0, stopIndex: int = None, service: MessageService = Depends()):
    messages = service.getMessages(user, startIndex, stopIndex)
    if messages is None:
        raise HTTPException(status_code=404, detail="No messages found.")
    return messages

@messageRouter.delete("/messages/{messageID}")
async def delete_message(messageID: str, service: MessageService = Depends()):
    result = service.deleteMessage(messageID)
    if not result:
        raise HTTPException(status_code=404, detail="Message not found.")
    return {"detail": "Message deleted successfully"}

@messageRouter.delete("/messages/")
async def delete_messages(messagesID: List[str], service: MessageService = Depends()):
    if not messagesID:
        raise HTTPException(status_code=400, detail="No message IDs provided.")
    
    service.deleteMessages(messagesID)
    return {"detail": "Messages deleted successfully"}