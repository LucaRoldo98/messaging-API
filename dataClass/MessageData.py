from uuid import UUID
from datetime import datetime
from typing import Optional

class MessageData:
    def __init__(self,
                 sender: str,
                 recipient: str,
                 message: str,
                 id: Optional[int] = None,
                 timestamp: Optional[datetime] = None,
                 is_fetched: Optional[bool] = False):

        self.id = id
        self.recipient = recipient
        self.sender = sender
        self.message = message
        self.timestamp = timestamp
        self.is_fetched = is_fetched
