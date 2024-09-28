from persistance.repository.IRepository import IRepository
from persistance.repository.SQLRepository import SQLRepository
from sqlalchemy.orm import Session
from fastapi import Depends
from config.database import SessionLocal

def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def get_repository(session: Session = Depends(get_db_session)) -> IRepository:
    return SQLRepository(session)
