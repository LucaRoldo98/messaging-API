from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from config.database import Base
import uuid

class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(String(128), default=lambda: uuid.uuid4().hex, nullable=False, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    
    sent_messages = relationship("MessageModel", foreign_keys="[MessageModel.sender]", back_populates="sender_user")
    received_messages = relationship("MessageModel", foreign_keys="[MessageModel.recipient]", back_populates="recipient_user")