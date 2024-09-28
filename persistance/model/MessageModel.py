from sqlalchemy import Column, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
import datetime
import uuid

class MessageModel(Base):
    __tablename__ = "messages"
    
    id = Column(String(128), default=lambda: uuid.uuid4().hex, nullable=False, primary_key=True, index=True)
    sender = Column(String(128), ForeignKey('users.id'), nullable=False)
    recipient = Column(String(128), ForeignKey('users.id'), nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    is_fetched = Column(Boolean, default=False)
    sender_user = relationship("UserModel", foreign_keys=[sender], back_populates="sent_messages")
    recipient_user = relationship("UserModel", foreign_keys=[recipient], back_populates="received_messages")