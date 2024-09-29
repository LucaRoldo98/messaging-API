from persistance.repository.IUserRepository import IUserRepository
from fastapi import Depends
from dataClasses.UserData import UserData
from typing import Optional
from config.dependencies import get_user_repository

class UserService: 
    _userRepository: IUserRepository
    
    def __init__(self, repository: IUserRepository = Depends(get_user_repository)):
        self._userRepository = repository
        
    def createUser(self, user: UserData) -> UserData:
        return self._userRepository.create(user)
    
    def getUserByID(self, userID: str) -> Optional[UserData]:
        return self._userRepository.getByID(userID)
    
    def getUserByEmail(self, email: str) -> Optional[UserData]:
        return self._userRepository.getByEmail(email)
                
    def deleteUser(self, userID: str):
        return self._userRepository.delete(userID)