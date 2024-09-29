from persistance.repository.IMessageRepository import IMessageRepository
from persistance.repository.IUserRepository import IUserRepository
from fastapi import Depends
from dataClasses.MessageData import MessageData
from typing import Optional, List
from config.dependencies import get_message_repository, get_user_repository
class MessageService: 
    _messageRepository: IMessageRepository
    _userRepository: IUserRepository
    
    def __init__(self, messageRepository: IMessageRepository = Depends(get_message_repository), userRepository: IUserRepository = Depends(get_user_repository)):
        self._messageRepository = messageRepository
        self._userRepository = userRepository
        
    def submitMessage(self, message: MessageData) -> Optional[MessageData]:
        sender = self._userRepository.get(message.sender)
        if not sender:
            return None

        recipient = self._userRepository.get(message.recipient)
        if not recipient:
            return None

        return self._messageRepository.create(message)            
    
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