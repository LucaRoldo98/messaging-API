from sqlalchemy import Column, String, Boolean, DateTime, Text
from config.database import Base
import datetime
import uuid
class MessageModel(Base):
    __tablename__ = "messages"
    
    id = Column(String(128), default=uuid.uuid4, nullable=False, primary_key=True, index=True)
    sender = Column(String(100))
    recipient = Column(String(100))
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    is_fetched = Column(Boolean, default=False)