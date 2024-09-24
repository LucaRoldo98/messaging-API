from abc import ABC, abstractmethod
from dto.message_dto import MessageDTO
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class IRepository(ABC):
    @abstractmethod
    def addMessage(self, message: MessageDTO) -> Optional[MessageDTO]:
        """
        Adds a message to the repository.
        Returns the added message, or None if failed.
        """
        pass
    
    @abstractmethod
    def getNewMessages(self, name: str) -> List[MessageDTO]:
        """
        Fetches new messages for the recipient.
        Returns an empty list if no new messages are found.
        """
        pass
    
    @abstractmethod
    def getMessages(self, startTime: datetime, stopTime: datetime) -> List[MessageDTO]:
        """
        Fetches messages within the given time range.
        Returns an empty list if no messages are found.
        """
        pass
    
    @abstractmethod
    def deleteMessages(self, messagesId : List[UUID]) -> None:
        """
        Deletes messages with the given UUIDs.
        """
        pass
    
    