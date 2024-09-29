from datetime import datetime
from typing import Optional

class MessageData:
    """
    Represents a message in the messaging service.
    This class is decoupled from the controller and repository layers,
    allowing for clean data handling throughout the application.
    """
    
    def __init__(self,
                 sender: Optional[str],
                 recipient: Optional[str],
                 text: str,
                 id: Optional[str] = None,
                 timestamp: Optional[datetime] = None,
                 is_fetched: Optional[bool] = False):

        self.id = id
        self.recipient = recipient
        self.sender = sender
        self.text = text
        self.timestamp = timestamp
        self.is_fetched = is_fetched
        
    def __repr__(self) -> str:
        return (
            f"""Message with id={self.id}, 
            sender={self.sender}, 
            recipient={self.recipient}, 
            text={self.text}, 
            timestamp={self.timestamp}, 
            is_fetched={self.is_fetched}"""
        )
