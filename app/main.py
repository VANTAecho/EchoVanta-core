from fastapi import FastAPI
from pydantic import BaseModel
from .models import Bot, SessionLocal

app = FastAPI()

class BotIn(BaseModel):
    name: str
    type: str
    platform: str
    config: dict

@app.post("/bots/")
def register_bot(bot: BotIn):
    db = SessionLocal()
    new_bot = Bot(**bot.dict())
    db.add(new_bot)
    db.commit()
    db.refresh(new_bot)
    db.close()
    return {"id": new_bot.id, "status": "registered"}
