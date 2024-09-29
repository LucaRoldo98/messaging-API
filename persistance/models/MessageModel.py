from sqlalchemy import Column, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
import datetime
import uuid
from dataClasses.MessageData import MessageData

class MessageModel(Base):
    __tablename__ = "messages"
    
    id = Column(String(128), default=lambda: uuid.uuid4().hex, nullable=False, primary_key=True, index=True)
    sender_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    recipient_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    text = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    is_fetched = Column(Boolean, default=False)
    
    sender = relationship("UserModel", foreign_keys=[sender_id], back_populates="sent_messages")
    recipient = relationship("UserModel", foreign_keys=[recipient_id], back_populates="received_messages")
    
    def toData(self):
        return MessageData(id=self.id, 
                           sender=self.sender_id, 
                           recipient=self.recipient_id, 
                           text=self.text, 
                           timestamp=self.timestamp,
                           is_fetched=self.is_fetched)