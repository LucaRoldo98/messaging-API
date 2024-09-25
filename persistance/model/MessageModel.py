from sqlalchemy import Column, UUID, String, Boolean, DateTime, Text
from config.database import Base
from datetime import datetime
import uuid

class MessageModel(Base):
    __tablename__ = "messages"
    
    id = Column(UUID, default=uuid.uuid4, nullable=False, primary_key=True, index=True)
    sender = Column(String(100))
    recipient = Column(String(100))
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    is_fetched = Column(Boolean, default=False)