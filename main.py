from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from utils.schemas import ChatMessage
from utils.response import get_response

app = FastAPI()

# a simple list for chat history
chat_history = []

@app.post("/chat")
async def chat_endpoint(chat_message: ChatMessage):
    chat_history.append({"role": "user", "content": chat_message.message})
    response = await get_response(chat_message.message, chat_history)
    chat_history.append({"role": "assistant", "content": response})
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)