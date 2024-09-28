from persistance.repository.IRepository import IRepository
from persistance.repository.SQLRepository import SQLRepository
from fastapi import Depends
from dataClasses.MessageData import MessageData
from typing import Optional, List
from config.dependencies import get_repository
class MessageService: 
    _messageRepository: IRepository
    
    def __init__(self, repository: IRepository = Depends(get_repository)):
        self._messageRepository = repository
        
    def submitMessage(self, message: MessageData) -> MessageData:
        savedMessage = self._messageRepository.create(message)
        return savedMessage
    
    def getUnreadMessages(self, user: str) ->  List[MessageData]:
        messages = self._messageRepository.get(user, isFetched=False)
        if messages:
            self._messageRepository.update([msg.id for msg in messages], newFetchedStatus=True)
        return messages
    
    def getMessages(self, user: str, startIndex: Optional[int], stopIndex: Optional[int]) -> List[MessageData]:
        messages = self._messageRepository.get(user, startIndex=startIndex, stopIndex=stopIndex)
        if messages:
            self._messageRepository.update([msg.id for msg in messages], newFetchedStatus=True)
        return messages
            
    def deleteMessage(self, messageID: str):
        return self._messageRepository.delete([messageID])
    
    def deleteMessages(self, messagesID: List[str]):
        return self._messageRepository.delete(messagesID)