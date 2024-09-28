from persistance.repository.IUserRepository import IUserRepository
from fastapi import Depends
from dataClasses.UserData import UserData
from typing import Optional, List
from config.dependencies import get_user_repository

class MessageService: 
    _userRepository: IUserRepository
    
    def __init__(self, repository: IUserRepository = Depends(get_user_repository)):
        self._userRepository = repository
        
    def createUser(self, user: UserData) -> UserData:
        return self._userRepository.create(user)
    
    def getUser(self, userID: str) -> Optional[UserData]:
        return self._userRepository.get(userID)
                
    def deleteUser(self, userID: str):
        return self._userRepository.delete(userID)