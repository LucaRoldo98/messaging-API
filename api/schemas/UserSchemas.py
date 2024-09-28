from pydantic import BaseModel, EmailStr

class UserCreateSchema(BaseModel):
    email: EmailStr

class UserResponseSchema(BaseModel):
    id: str
    email: EmailStr
        
class DeleteResponseSchema(BaseModel):
    detail : str

def userDataToSchema(user_data) -> UserResponseSchema:
    return UserResponseSchema(
        id=user_data.id,
        email=user_data.email
    )
