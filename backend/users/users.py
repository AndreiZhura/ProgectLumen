from fastapi import APIRouter

router = APIRouter()

@router.get("/user/{user_id}")
async def get_user(user_id: int):
    return{"message":f"Пользователь с ID: {user_id}"}

@router.get("/search/")
async def search(q: str = None):
    if q:
        return {"results": f"Результаты поиска по запросу: {q}"}
    return {"results": "Пустой запрос поиска"}