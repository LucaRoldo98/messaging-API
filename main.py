from sqlalchemy.orm import Session
from config.database import SessionLocal
from persistance.repository.SQLRepository import SQLRepository
from dataClass.MessageData import MessageData
import datetime
from config.database import Base, engine

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_repository():
    db: Session = next(get_db_session())

    repository = SQLRepository(db)

    # Create a new message
    new_message = MessageData(
        sender="Alice",
        recipient="Bob",
        message="Hello, Bob!"
    )

    # Add the message to the repository
    print("Adding new message to the repository:")
    repository.addMessage(new_message)

    # Fetch unread messages for Bob
    print("Fetching unread messages for Bob:")
    unread_messages = repository.getUnreadMessagesByUser("Bob")
    for msg in unread_messages:
        print(msg.message)

    # Mark the message as read
    print("Marking messages as read:")
    repository.markMessagesAsRead([new_message.id])

    # Fetch the same messages to verify they've been marked as read
    print("Fetching updated messages for Bob:")
    updated_messages = repository.getUnreadMessagesByUser("Bob")
    if not updated_messages:
        print("No unread messages found (messages have been marked as read).")
        
    print("Fetching messages with pagination:")

    paginated_messages = repository.getMessages(startIndex=1, stopIndex=10)
    for msg in paginated_messages:
        print(f"Message: {msg.message} (From: {msg.id})")

    # Delete the message
    print("Deleting messages from the repository:")
    repository.deleteMessages([new_message.id])

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    test_repository()
