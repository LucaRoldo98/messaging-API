from persistance.repository.IRepository import IRepository
from persistance.model.MessageModel import MessageModel
from sqlalchemy.orm import Session
from dataClasses.MessageData import MessageData
from typing import Optional, List

class SQLRepository(IRepository):
    session: Session
    
    def __init__(self, session: Session):
        self.session = session
        
    def addMessage(self, message: MessageData) -> Optional[MessageData]:
        db_message = MessageModel(
            sender = message.sender,
            recipient = message.recipient,
            message = message.message
            )
        self.session.add(db_message)
        try:
            self.session.commit()
            return message
        except:
            self.session.rollback()
            return 
        
    def getUnreadMessages(self, user: str) -> List[MessageData]:
        db_messages = self.session.query(MessageModel).filter(
            MessageModel.recipient == user, MessageModel.is_fetched == False
            ).order_by(MessageModel.timestamp).all()
        return [self._messageModelToData(msg) for msg in db_messages]
    
    def getMessages(self, user: str, stopIndex: Optional[int], startIndex: Optional[int]) -> List[MessageData]:
        
        if stopIndex is None:
            db_messages = (
                self.session.query(MessageModel)
                .filter(MessageModel.recipient == user)
                .order_by(MessageModel.timestamp)
                .offset(startIndex)
                .all()
            )
        else:
            if startIndex < 0 or stopIndex <= startIndex:
                return []

            limit = stopIndex - startIndex

            db_messages = (
                self.session.query(MessageModel)
                .filter(MessageModel.recipient == user)
                .order_by(MessageModel.timestamp)
                .offset(startIndex)
                .limit(limit)
                .all()
            )

        return [self._messageModelToData(msg) for msg in db_messages]

    def markMessagesAsRead(self, messagesID: List[str]) -> List[MessageData]:
        db_messages = self.session.query(MessageModel).filter(
            MessageModel.id.in_(messagesID)
        ).all()

        if not db_messages:
            return []

        for db_message in db_messages:
            db_message.is_fetched = True

        self.session.commit()
        return [self._messageModelToData(msg) for msg in db_messages]

    def deleteMessages(self, messagesID: List[str]) -> None:
        self.session.query(MessageModel).filter(MessageModel.id.in_(messagesID)).delete(synchronize_session=False)
        self.session.commit()
        
    def _messageDataToModel(self, message: MessageData) -> MessageModel:
        return MessageModel(
            sender=message.sender,
            recipient=message.recipient,
            message=message.message,
            id=message.id,
            timestamp=message.timestamp,
            is_fetched=message.is_fetched
        )
    
    def _messageModelToData(self, message: MessageModel) -> MessageData:
        return MessageData(
            sender=message.sender,
            recipient=message.recipient,
            message=message.message,
            id=message.id,
            timestamp=message.timestamp,
            is_fetched=message.is_fetched
        )