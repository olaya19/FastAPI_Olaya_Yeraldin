# views/massage_create.py
from fastapi import APIRouter
from controllers.massage_controller import create_massage
from redis_client import redis_client  



router = APIRouter()

@router.post("/")
async def add_massage(session: str, therapist: str, schedule: str):
    massage = create_massage(session, therapist, schedule)
    await redis_client.delete("massage_list")  # invalidar cache
    return {"message": "Massage created", "data": massage.__dict__}
