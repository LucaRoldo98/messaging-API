from persistance.repository.IRepository import IRepository
from fastapi import Depends
from dataClass.MessageData import MessageData
from typing import Optional, List

class MessageService: 
    _messageRepository: IRepository
    
    def __init__(self, repository: IRepository = Depends()):
        self._messageRepository = repository
        
    def submitMessage(self, message: MessageData) -> Optional[MessageData]:
        return self._messageRepository.addMessage(message)
    
    def getUnreadMessages(self, user: str) ->  List[MessageData]:
        messages = self._messageRepository.getUnreadMessages(user)
        self._messageRepository.markMessagesAsRead([msg.id for msg in messages])
        return messages
    
    def getMessages(self, user: str, startIndex: Optional[int], stopIndex: Optional[int]) -> List[MessageData]:
        return self._messageRepository.getMessages(user=user, startIndex=startIndex, stopIndex=stopIndex)
        
    def deleteMessage(self, messageID: str):
        return self._messageRepository.deleteMessages([messageID])
    
    def deleteMessages(self, messagesID: List[str]):
        return self._messageRepository.deleteMessages(messagesID)