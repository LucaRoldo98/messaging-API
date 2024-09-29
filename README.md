# Messaging-API

## Project Overview

This project is a simple messaging API that allows users to send and retrieve messages.
The API built in Python using **FastAPI** and **SQLAlchemy**, as well as **pydantic** for data validation. The API stores messages and users in a **SQLite** database.
It follows a **repository-service-controller pattern** for separation of concerns between the business logic, data access, and controller layers.


### Core Features

- Users can register with an email address.
- Messages can be submitted between registered users by specifying the sender, the recipient and the text.
- Messages can be retrieved, both as unread messages and as paginated messages (with a start and stop index), sorted by decreasing time order.
- Messages can be deleted, both one by one or with a bulk operation.

## Project Structure

- **api**: Defines the API endpoints as routers (controllers), as well as request/response schemas.
- **services**: Manages business logic for messages and users.
- **persistance**: Contains data access logic. Repositories handle storage operations and access, while the models define the structure and relationships of database tables. Repositories must implement their respective interfaces (eg. `IMessageRepository` and `IUserRepository`), allowing for repository dependencies to be easily swapped at the service level for decoupling, flexibility, and easier testing, without changing the core business logic. 
- **dataClasses**: Defines repository-agnostic classes for users and messages to decouple the service layer from a specific repository implementation (ex. SQL or CSV).
- **config**: Includes the database setup and project dependencies.

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip3 install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    python3 main.py
    ```
    The application will be then avaliable at `http://127.0.0.1:8000/`
5. **Access API Documentation**:
    Open your browser and navigate to:
    ```
    http://127.0.0.1:8000/docs
    ```
    This will show the interactive API documentation via Swagger UI.

## How the API Works

1. **Create a user**:
    Before creating or sending messages, you need to create a user by specifying its email:
    - Method: `POST`
    - Endpoint: `/user/`
    - Payload:
      ```json
      {
        "email": "user@example.com"
      }
      ```
    This registers a user with the provided email address. The API will raise a HTTPException if an users already exists with the same email.

2. **Send a message**:
    To send a message, the sender and recipient must both be registered users.
    - Method: `POST`
    - Endpoint: `/messages/`
    - Payload:
      ```json
      {
        "senderID": "string",
        "recipientID": "string",
        "text": "string"
      }
      ```
      The userID is provided as response from the create user endpoint. To retrieve it again, you can call the GET `/user/email/{email}` endpoint, and the API will provide you the userID. The API will raise a 404 HTTPException if the user with the specified senderID and/or recipentID does not exist in the database.

3. **Fetch new messages**:
    Retrieve all unread messages by recipient ID:
    - Method: `GET`
    - Endpoint: `/messages/unread/{userID}`
    Messages are returned in descending time order (most recent first). The API will raise a 404 HTTPException if the user with the specified userID does not exist in the database.
  
4. **Fetching all messages (with pagination)**:
    Retrieve messages by recipient ID. Optionally, you can specify a start and/or stop index, to retrieve the messages within the specified index range:
    - Method: `GET`
    - Endpoint: `/messages/{userID}`

   Query Parameters (Optional):
    - **startIndex**: Start index of the messages to retrieve.
    - **stopIndex**: End index of the messages to retrieve.
   Messages are returned in descending time order (most recent first). The API will raise a 404 HTTPException if the user with the specified userID does not exist in the database.

5. **Delete a single message**:
    Delete a message by specifying the messageID:
    - Method: `DELETE`
    - Endpoint: `/messages/{messageID}`
    The API will raise a 404 HTTPException if the messageID does not match any message in the database. 

6. **Delete multiple messages**:
    Bulk deletes messages.
   
    - Method: `DELETE`
    - Endpoint: `/messages/`
    - Payload:
      ```json
      {
        "messagesID": ["string"]
      }
      ```
    The API will raise a 404 HTTPException if none of the specified messagesID matches a message in the database, otherwise it will return a message specifying the number of messages deleted. 

7. **Get User by ID**:
    Fetches a user by their userID.
    - Method: `GET`
    - Endpoint: `/user/id/{userID}`
    The API will raise a 404 HTTPException if the user with the specified userID does not exist in the database.
  
8. **Get User by email**:
    Fetches a user by their email address.
    - Method: `GET`
    - Endpoint: `/user/email/{email}`
    The API will raise a 404 HTTPException if the user with the specified email does not exist in the database.
  
9. **Delete User by ID**:
    Deletes a user by their userID.
    - **Method**: `DELETE`
    - **Endpoint**: `/user/{userID}`
   The API will raise a 404 HTTPException if the user with the specified userID does not exist in the database.

## Notes

The system requires a user to be created before it can send/receive any message.
When sending a message, both `sender_id` and `recipient_id` must be valid user IDs. 
