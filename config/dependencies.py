from persistance.repository.IMessageRepository import IUserRepository
from persistance.repository.SQLMessageRepository import SQLMessageRepository
from sqlalchemy.orm import Session
from fastapi import Depends
from config.database import get_db_session

def get_message_repository(session: Session = Depends(get_db_session)) -> IUserRepository:
    return SQLMessageRepository(session)
