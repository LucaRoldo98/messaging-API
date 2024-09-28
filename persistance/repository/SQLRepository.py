from persistance.repository.IRepository import IRepository
from persistance.model.MessageModel import MessageModel
from sqlalchemy.orm import Session
from dataClasses.MessageData import MessageData
from typing import Optional, List

class SQLRepository(IRepository):
    session: Session
    
    def __init__(self, session: Session):
        self.session = session
        
    def create(self, message: MessageData) -> MessageData:
        db_message = MessageModel(
            sender = message.sender,
            recipient = message.recipient,
            text = message.text
            )
        self.session.add(db_message)
        self.session.commit()
        return db_message.toData()
        
    def get(self, user: str, isFetched: Optional[bool] = None, startIndex: Optional[int] = None, stopIndex: Optional[int] = None) -> Optional[List[MessageData]]:
        query = self.session.query(MessageModel).filter(MessageModel.recipient == user).order_by(MessageModel.timestamp.desc())
        
        if query.first() is None:
            return None
        
        if isFetched is not None:
            query = query.filter(MessageModel.is_fetched == isFetched)

        if startIndex is not None:
            query = query.offset(startIndex)

        if stopIndex is not None:
            limit = stopIndex - (startIndex if startIndex is not None else 0)
            query = query.limit(limit)

        db_messages = query.all()
        return [msg.toData() for msg in db_messages]

    def update(self, messagesID: List[str], newFetchedStatus: bool) -> List[MessageData]:
        db_messages = self.session.query(MessageModel).filter(
            MessageModel.id.in_(messagesID)
        ).all()
        
        if newFetchedStatus is not None:
            for db_message in db_messages:
                db_message.is_fetched = newFetchedStatus
                
        self.session.commit()
        return [msg.toData() for msg in db_messages]


    def delete(self, messagesID: List[str]) -> int:
        deletedCount = self.session.query(MessageModel).filter(MessageModel.id.in_(messagesID)).delete()
        self.session.commit()
        return deletedCount