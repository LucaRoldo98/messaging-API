from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from config.database import Base
import datetime

class MessageModel(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True, index=True)
    sender = Column(String(100))
    recipient = Column(String(100))
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    is_fetched = Column(Boolean, default=False)