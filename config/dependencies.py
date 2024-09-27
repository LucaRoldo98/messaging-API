from persistance.repository.IRepository import IRepository
from persistance.repository.SQLRepository import SQLRepository
from sqlalchemy.orm import Session
from fastapi import Depends
from config.database import get_db_session

def get_repository(session: Session = Depends(get_db_session)) -> IRepository:
    return SQLRepository(session)
