from abc import ABC, abstractmethod
from dataClass.MessageData import MessageData
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class IRepository(ABC):
    @abstractmethod
    def addMessage(self, message: MessageData) -> Optional[MessageData]:
        """
        Adds a message to the repository.
        Returns the added message, or None if failed.
        """
        raise NotImplementedError
    
    @abstractmethod
    def getNewMessages(self, user: str) -> List[MessageData]:
        """
        Fetches new messages for the recipient.
        Returns an empty list if no new messages are found.
        """
        raise NotImplementedError
    
    @abstractmethod
    def updateMessages(self, ) -> List[MessageData]:
        """
        Fetches new messages for the recipient.
        Returns an empty list if no new messages are found.
        """
        raise NotImplementedError
    
    @abstractmethod
    def getMessages(self, startTime: datetime, stopTime: datetime) -> List[MessageData]:
        """
        Fetches messages within the given time range.
        Returns an empty list if no messages are found.
        """
        raise NotImplementedError
    
    @abstractmethod
    def deleteMessages(self, messagesId : List[UUID]) -> None:
        """
        Deletes messages with the given UUIDs.
        """
        raise NotImplementedError
    
    