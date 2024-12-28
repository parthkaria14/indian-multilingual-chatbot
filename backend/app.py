from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .chatbot import chatbot_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    language: str = "en"

@app.get("/")
async def home():
    return {"message": "Welcome to the Multilingual Chatbot API"}

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    try:
        response = chatbot_response(chat_request.message, chat_request.language)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
