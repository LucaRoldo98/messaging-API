from abc import ABC, abstractmethod
from dataClasses.MessageData import MessageData
from typing import List, Optional
class IRepository(ABC):
    @abstractmethod
    def create(self, message: MessageData) -> MessageData:
        """
        Adds a message to the repository.
        Returns the added message.
        """
        raise NotImplementedError
    
    @abstractmethod
    def get(self, user: str, isFetched: Optional[bool], startIndex: Optional[int], stopIndex: Optional[int]) -> List[MessageData]:
        """
        Gets messages for given user, sorted by descending timestamp.
        The method can take some optional filters:
        - isFetched: Get only messages with the speficified fetched status.
        - startIndex: Get results starting from specified index. Default value is 0.
        - stopIndex: Get results up to the specified index. 
        Returns an empty list if no messages are found.
        """
        raise NotImplementedError
    
    @abstractmethod
    def update(self, messagesID: List[str], newFetchedStatus: bool) -> List[MessageData]:
        """
        Update the messages with the given IDs.
        Updates can be done on the following fields:
        - is_fetched, according to the value specified in newFetchedStatus
        Returns the updated messages, or an empty list if no messages were updated.
        """
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, messagesID: List[str]) -> None:
        """
        Deletes the given messages.
        """
        raise NotImplementedError
    
    