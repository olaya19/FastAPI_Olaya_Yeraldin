# views/massage_list.py
from fastapi import APIRouter
from controllers.massage_controller import get_all_massages
from redis_client import redis_client  


router = APIRouter()

@router.get("/")
async def list_massages():
    cached = await redis_client.get("massage_list")
    if cached:
        return {"data": eval(cached), "source": "cache"}
    data = get_all_massages()
    await redis_client.set("massage_list", str([m.__dict__ for m in data]), ex=60)
    return {"data": [m.__dict__ for m in data], "source": "db"}
