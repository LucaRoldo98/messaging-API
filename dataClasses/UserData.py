from typing import Optional

class UserData:
    """
    Represents a user in the user service.
    This class is decoupled from the controller and repository layers,
    allowing for clean data handling throughout the application.
    """
    
    def __init__(self,
                 email : str,
                 id: Optional[str] = None,
                 ):

        self.id = id
        self.email = email
        self.received_messages = []
                
    def __repr__(self) -> str:
        return (
            f"""User with id={self.id}, 
            email={self.email}"""
        )
