from pydantic import BaseModel, EmailStr
from dataClasses.UserData import UserData

class UserCreateSchema(BaseModel):
    email: EmailStr

class UserResponseSchema(BaseModel):
    id: str
    email: EmailStr
        
class UserDeleteResponseSchema(BaseModel):
    detail : str

def userDataToSchema(userData: UserData) -> UserResponseSchema:
    return UserResponseSchema(
        id=userData.id,
        email=userData.email
    )
