from fastapi import FastAPI, HTTPException, Depends, status
from api.router import message_router

app = FastAPI()

app.include_router(message_router.MessageRouter)