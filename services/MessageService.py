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
    
    def getUnreadMessages(self, userID: str) -> Optional[List[MessageData]]:
        receivedMessages = self._userRepository.getReceivedMessages(userID)
    
        if receivedMessages is None: 
            return None
        
        receivedMessages = [msg for msg in receivedMessages if msg.is_fetched == False]
        self._messageRepository.update([msg.id for msg in receivedMessages], newFetchedStatus=True)

        return receivedMessages
    
    def getMessages(self, userID: str, startIndex: Optional[int], stopIndex: Optional[int]) -> List[MessageData]:
        receivedMessages = self._userRepository.getReceivedMessages(userID)
        if receivedMessages is None:
            return None
        
        if startIndex is not None:
            receivedMessages = receivedMessages[startIndex:]

        if stopIndex is not None:
            receivedMessages = receivedMessages[:stopIndex - (startIndex if startIndex is not None else 0)]
        
        self._messageRepository.update([msg.id for msg in receivedMessages], newFetchedStatus=True)
        return receivedMessages
            
    def deleteMessage(self, messageID: str):
        return self._messageRepository.delete([messageID])
    
    def deleteMessages(self, messagesID: List[str]):
        return self._messageRepository.delete(messagesID)