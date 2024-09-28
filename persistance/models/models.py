from sqlalchemy import Column, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
import datetime
import uuid

class MessageModel(Base):
    __tablename__ = "messages"
    
    id = Column(String(128), default=lambda: uuid.uuid4().hex, nullable=False, primary_key=True, index=True)
    sender_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    recipient_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    is_fetched = Column(Boolean, default=False)
    
    sender = relationship("UserModel", foreign_keys=[sender_id], back_populates="sent_messages")
    recipient = relationship("UserModel", foreign_keys=[recipient_id], back_populates="received_messages")
    
class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(String(128), default=lambda: uuid.uuid4().hex, nullable=False, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    sent_messages = relationship("MessageModel", back_populates="sender", foreign_keys="[MessageModel.sender_id]")
    received_messages = relationship("MessageModel", back_populates="recipient", foreign_keys="[MessageModel.recipient_id]")