from persistance.repository.IRepository import IRepository
from fastapi import Depends
from dataClasses.MessageData import MessageData
from typing import Optional, List

class MessageService: 
    _messageRepository: IRepository
    
    def __init__(self, repository: IRepository = Depends()):
        self._messageRepository = repository
        
    def submitMessage(self, message: MessageData) -> MessageData:
        if not message.sender or not message.recipient or not message.message:
            raise ValueError("Sender, recipient and message are required")
        savedMessage = self._messageRepository.addMessage(message)
        if not savedMessage:
            raise RuntimeError(f"Failed to submit the message {message}.")
        return savedMessage
    
    def getUnreadMessages(self, user: str) ->  List[MessageData]:
        messages = self._messageRepository.getUnreadMessages(user)
        if messages:
            self._messageRepository.markMessagesAsRead([msg.id for msg in messages])
        return messages
    
    def getMessages(self, user: str, startIndex: Optional[int], stopIndex: Optional[int]) -> List[MessageData]:
        return self._messageRepository.getMessages(user=user, startIndex=startIndex, stopIndex=stopIndex)
        
    def deleteMessage(self, messageID: str):
        return self._messageRepository.deleteMessages([messageID])
    
    def deleteMessages(self, messagesID: List[str]):
        return self._messageRepository.deleteMessages(messagesID)