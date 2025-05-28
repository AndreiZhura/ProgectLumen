from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from users.users import router as user_router


app = FastAPI()

origins = [
    "http://localhost:5500",   # адрес твоего фронтенда, например
    "http://127.0.0.1:5500",
    # Можно добавить другие, или просто "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # или ["*"] для разрешения с любых адресов
    allow_credentials=True,
    allow_methods=["*"],    # разрешаем все методы, включая OPTIONS
    allow_headers=["*"],    # разрешаем все заголовки
)

@app.get("/")
async def root():
   
    return {"message": f"Привет, я Lumen! я только учусь "}


class Userinput(BaseModel):
    name:str

@app.post("/hello")
async def hello(user:Userinput):
    return {"message": f"Привет, {user.name}! Я Lumen."}

app.include_router(user_router)