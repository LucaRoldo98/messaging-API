from fastapi import FastAPI
from api.routers.MessageRouter import messageRouter
from api.routers.UserRouter import userRouter
from config.database import init_db
import uvicorn

app = FastAPI()
app.include_router(messageRouter)
app.include_router(userRouter)

@app.get("/")
async def health_check():
    return {"status": "API is running"}

if __name__ == "__main__":
    init_db()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)