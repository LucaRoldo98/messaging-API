from uuid import UUID
from datetime import datetime

class MessageDTO:
    def __init__(self, id: UUID, sender: str, recipient: str, message: str, timestamp: datetime, is_fetched: bool):
        self.id = id
        self.recipient = recipient
        self.sender = sender
        self.message = message
        self.timestamp = timestamp
        self.is_fetched = is_fetched
