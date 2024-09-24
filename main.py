from fastapi import FastAPI
from routers import message_router

app = FastAPI()
app.include_router(message_router.MessageRouter)