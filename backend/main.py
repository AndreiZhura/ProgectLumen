from fastapi import FastAPI, Request
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/"

@app.get("/")
async def root():
    return {"message": "Бот Lumen запущен"}

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_text = data["message"].get("text", "")

        from lumen_core.logic.reasoner import generate_reply
        reply = generate_reply(user_text)
        send_message(chat_id, reply)

    return {"ok": True}

def send_message(chat_id, text):
    resp = requests.post(
        BOT_API_URL + "sendMessage",
        json={"chat_id": chat_id, "text": text}
    )
    if not resp.ok:
        print(f"Ошибка при отправке сообщения: {resp.status_code} {resp.text}")
