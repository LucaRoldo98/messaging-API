from fastapi import APIRouter, HTTPException, Depends, status
from services.UserService import UserService
from dataClasses.UserData import UserData
from api.schemas.UserSchemas import *

userRouter = APIRouter(prefix="/user")

@userRouter.post("/", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreateSchema, service: UserService = Depends()):
    userData = service.createUser(UserData(**user.model_dump()))
    if userData is None: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with email {user.email} already exists")
    return userDataToSchema(userData)

@userRouter.get("/id/{userID}", response_model=UserResponseSchema)
async def get_user(userID : str, service: UserService = Depends()):    
    user = service.getUserByID(userID) 
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {userID} does not exist")
    return userDataToSchema(user)

@userRouter.get("/email/{email}", response_model=UserResponseSchema)
async def get_user(email: str, service: UserService = Depends()):
    user = service.getUserByEmail(email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with email {email} does not exist")
    return userDataToSchema(user)

@userRouter.delete("/{userID}", response_model=UserDeleteResponseSchema)
async def delete_user(userID: str, service: UserService = Depends()):
    deleted_count = service.deleteUser(userID)
    if deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {userID} does not exist")
    return UserDeleteResponseSchema(detail="User deleted successfully")