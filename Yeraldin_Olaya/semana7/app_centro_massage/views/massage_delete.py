# views/massage_delete.py
from fastapi import APIRouter
from controllers.massage_controller import delete_massage
from redis_client import redis_client  



router = APIRouter()

@router.delete("/{massage_id}")
async def delete_massage_view(massage_id: int):
    massage = delete_massage(massage_id)
    await redis_client.delete("massage_list")
    return {"message": "Massage deleted", "data": massage.__dict__ if massage else None}
