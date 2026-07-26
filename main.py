from agent.graph import run_agent
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"),name="static")

class ChatRequest(BaseModel):
    session_id : str
    message : str

class ChatResponse(BaseModel):
    reply : str

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

@app.post("/chat",response_model=ChatResponse)
def chat(request : ChatRequest):
    reply = run_agent(request.message, request.session_id)
    return ChatResponse(reply=reply)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)