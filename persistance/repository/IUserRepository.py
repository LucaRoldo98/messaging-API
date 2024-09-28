from abc import ABC, abstractmethod
from typing import List, Optional
from dataClasses.UserData import UserData

class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: UserData) -> Optional[UserData]:
        """
        Create a new user in the repository.
        Returns the created user if the operation is successful.
        Returns None if the user already exists.
        """
        raise NotImplementedError
    
    @abstractmethod
    def get(self, userID: str) -> Optional[UserData]:
        """
        Gets user data given its ID.
        Returns None if the user with the specified ID does not exist.
        """
        raise NotImplementedError
    
    @abstractmethod
    def update(self, userID: str, newEmail: str) -> Optional[UserData]:
        """
        Update the email of the user with the specified userID.
        Returns the updated user if the operation is successful.
        Returns None if the user with the specified ID does not exist.
        """
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, userID: str) -> bool:
        """
        Deletes the given user.
        Returns True if the operation is successful.
        Returns False if the user with the specified ID does not exist.
        """
        raise NotImplementedError
    
    
    