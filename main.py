from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from services.trains import get_trains_with_segments
from services.ai_agent import ask_ai

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html") as f:
        return f.read()

@app.get("/search")
def search(source: str, destination: str, date: str):
    return {"results": get_trains_with_segments(source, destination, date)}

@app.get("/chat")
def chat(query: str):
    return {"response": ask_ai(query)}
