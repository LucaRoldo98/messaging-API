from persistance.repository.IUserRepository import IUserRepository
from persistance.models.UserModel import UserModel
from sqlalchemy.orm import Session
from dataClasses.UserData import UserData
from dataClasses.MessageData import MessageData
from typing import Optional, List

class SQLUserRepository(IUserRepository):
    session: Session
    
    def __init__(self, session: Session):
        self.session = session
        
    def create(self, user: UserData) -> Optional[UserData]:
        existing_user = self.session.query(UserModel).filter_by(email=user.email).first()
        if existing_user:
            return None
        db_user = UserModel(
            email = user.email
            )
        self.session.add(db_user)
        self.session.commit()
        return db_user.toData()
        
    def get(self, userID: str) -> Optional[UserData]:
        db_user = self.session.query(UserModel).filter(UserModel.id == userID).first()
        if db_user is None:
            return None
        return db_user.toData()
    
    def getReceivedMessages(self, userID: str) -> Optional[List[MessageData]]:
        user = self.session.query(UserModel).filter(UserModel.id == userID).first()

        if user is None:
            return None

        receivedMessages = user.received_messages
        return [msg.toData() for msg in receivedMessages]

            
    def update(self, userID: str, newEmail: str) -> Optional[UserData]:
        db_user = self.session.query(UserModel).filter(
            UserModel.id == userID
        ).first()
                
        if db_user is None:
            return None
        
        db_user.email = newEmail
        self.session.commit()
        return db_user.toData()


    def delete(self, userID: str) -> int:
        db_user = self.session.query(UserModel).filter(UserModel.id == userID).delete()
        if db_user == 0:
            return False
        self.session.commit()
        return True