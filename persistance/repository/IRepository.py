from abc import ABC, abstractmethod
from dataClass.MessageData import MessageData
from typing import List, Optional
class IRepository(ABC):
    @abstractmethod
    def addMessage(self, message: MessageData) -> Optional[MessageData]:
        """
        Adds a message to the repository.
        Returns the added message, or None if failed.
        """
        raise NotImplementedError
    
    @abstractmethod
    def getUnreadMessagesByUser(self, user: str) -> List[MessageData]:
        """
        Fetches unread messages for the recipient.
        Returns an empty list if no unread messages are found.
        """
        raise NotImplementedError
    
    @abstractmethod
    def getMessages(self, startIndex: int, stopIndex: int) -> List[MessageData]:
        """
        Fetches messages within the given time range.
        The startTime and stopTime can be omitted, to remove the lower and higher bounds, respectively.
        Returns an empty list if no messages are found.
        """
        raise NotImplementedError
    
    @abstractmethod
    def markMessagesAsRead(self, messagesID: List[str]) -> List[MessageData]:
        """
        Marks the messages with the given IDs as read.
        Returns the updated messages, or an empty list if no messages were updated.
        """
        raise NotImplementedError
    
    @abstractmethod
    def deleteMessages(self, messagesID: List[str]) -> None:
        """
        Deletes the given messages.
        """
        raise NotImplementedError
    
    