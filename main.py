from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Здесь можно указать конкретные домены, если нужно
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP методы
    allow_headers=["*"],  # Разрешить все заголовки
)

class Message(BaseModel):
    text: str

@app.post("/analyze")
def analyze(message: Message):
    anxiety_score = len(message.text) % 10
    return {"anxiety_score": anxiety_score}
