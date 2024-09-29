from persistance.repository.IMessageRepository import IMessageRepository
from persistance.repository.SQLMessageRepository import SQLMessageRepository
from persistance.repository.IUserRepository import IUserRepository
from persistance.repository.SQLUserRepository import SQLUserRepository
from sqlalchemy.orm import Session
from fastapi import Depends
from config.database import SessionLocal

def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def get_message_repository(session: Session = Depends(get_db_session)) -> IMessageRepository:
    return SQLMessageRepository(session)

def get_user_repository(session: Session = Depends(get_db_session)) -> IUserRepository:
    return SQLUserRepository(session)
