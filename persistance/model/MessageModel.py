from sqlalchemy import Column, String, Boolean, DateTime, Text
from config.database import Base
import datetime
import uuid
class MessageModel(Base):
    __tablename__ = "messages"
    
    id = Column(String, default=lambda: uuid.uuid4().hex, nullable=False, primary_key=True, index=True)
    sender = Column(String(100))
    recipient = Column(String(100))
    message = Column(Text)
    timestamp = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    is_fetched = Column(Boolean, default=False)