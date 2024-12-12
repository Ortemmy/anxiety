from fastapi import FastAPI
from pydantic import BaseModel

# Создаём приложение FastAPI
app = FastAPI()

# Модель данных, которая будет использоваться для запросов
class Message(BaseModel):
    text: str

# Маршрут API
@app.post("/analyze")
def analyze(message: Message):
    # Простая логика анализа (замените на вызов вашей модели)
    anxiety_score = len(message.text) % 10  # Пример: длина текста влияет на "оценку"
    return {"anxiety_score": anxiety_score}
