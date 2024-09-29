from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from config.database import Base
import uuid
from dataClasses.UserData import UserData

class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(String(128), default=lambda: uuid.uuid4().hex, nullable=False, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    sent_messages = relationship("MessageModel", back_populates="sender", foreign_keys="[MessageModel.sender_id]", order_by="MessageModel.timestamp.desc()")
    received_messages = relationship("MessageModel", back_populates="recipient", foreign_keys="[MessageModel.recipient_id]", order_by="MessageModel.timestamp.desc()")
    
    def toData(self) -> UserData:
        return UserData(id=self.id, email=self.email)