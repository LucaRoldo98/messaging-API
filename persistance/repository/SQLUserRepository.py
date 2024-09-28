from persistance.repository.IUserRepository import IUserRepository
from persistance.model.UserModel import UserModel
from sqlalchemy.orm import Session
from dataClasses.UserData import UserData
from typing import Optional, List

class SQLUserRepository(IUserRepository):
    session: Session
    
    def __init__(self, session: Session):
        self.session = session
        
    def create(self, user: UserData) -> UserData:
        db_user = UserModel(
            email = user.email
            )
        self.session.add(db_user)
        self.session.commit()
        return self._userModelToData(db_user)
        
    def get(self, userID: str) -> Optional[UserData]:
        db_user = self.session.query(UserModel).filter(UserModel.id == userID).first()
        
        if db_user is None:
            return None
        
        return self._userModelToData(db_user)

    def update(self, userID: str, newEmail: str) -> UserData:
        db_user = self.session.query(UserModel).filter(
            UserModel.id == userID
        ).first()
        
        if db_user is None:
            return None
        
        db_user.email = newEmail
        self.session.commit()
        return self._userModelToData(db_user)


    def delete(self, userID: List[str]) -> int:
        db_user = self.session.query(UserModel).filter(UserModel.id == userID).delete()
        if db_user == 0:
            return False
        self.session.commit()
        return True
    
    def _userModelToData(self, user: UserModel) -> UserData:
        return UserData(
            id=user.id,
            email=user.email
        )