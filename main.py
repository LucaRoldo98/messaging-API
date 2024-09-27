from sqlalchemy.orm import Session
from config.database import SessionLocal
from persistance.repository.SQLRepository import SQLRepository
from dataClasses.MessageData import MessageData
from config.database import init_db
from services.MessageService import MessageService

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_message_service():

    init_db()

    # Get a DB session
    db: Session = next(get_db_session())

    # Create an instance of the SQL repository
    repository = SQLRepository(db)

    # Create an instance of the MessageService
    service = MessageService(repository)

    # 1. Submit a new message
    for i in range(10):
        print("Submitting a new message:")
        new_message = MessageData(
            sender="Alice",
            recipient="Bob",
            message=f"Hello, Bob this message number {i}",
        )
        service.submitMessage(new_message)
        

    # 2. Get unread messages for Bob
    print("\nFetching unread messages for Bob:")
    unread_messages = service.getUnreadMessages("Bob")
    for msg in unread_messages:
        print(f"Unread message: {msg.message}")

    # # 3. Get paginated messages (startIndex = 0, stopIndex = 10)
    # print("\nFetching paginated messages (startIndex=0, stopIndex=10):")
    # paginated_messages = service.getMessages("Alice", startIndex=0, stopIndex=10)
    # for msg in paginated_messages:
    #     print(f"Message: {msg.message}, Timestamp: {msg.timestamp}")

    # # 4. Mark messages as read
    # print("\nMarking messages as read:")
    # service.getUnreadMessages("Bob")  # This marks them as read automatically

    # # 5. Fetch messages again to ensure they're marked as read
    # print("\nFetching unread messages for Bob again:")
    # updated_unread_messages = service.getUnreadMessages("Bob")
    # if not updated_unread_messages:
    #     print("No unread messages found (all messages have been marked as read).")

    # # 6. Delete a message by ID
    # print("\nDeleting a message:")
    # if unread_messages:  # Ensure there's a message to delete
    #     service.deleteMessage(unread_messages[0].id)
    #     print(f"Deleted message with ID: {unread_messages[0].id}")

    # # 7. Delete multiple messages by ID
    # print("\nDeleting multiple messages:")
    # service.deleteMessages([msg.id for msg in paginated_messages])
    # print(f"Deleted messages with IDs: {[msg.id for msg in paginated_messages]}")

if __name__ == "__main__":
    test_message_service()