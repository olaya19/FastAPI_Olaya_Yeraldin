# views/massage_update.py
from controllers.massage_controller import update_massage
from fastapi import APIRouter
from redis_client import redis_client

router = APIRouter()


@router.put("/{massage_id}")
async def update_massage_view(
    massage_id: int, session: str = None, therapist: str = None, schedule: str = None
):
    massage = update_massage(massage_id, session, therapist, schedule)
    await redis_client.delete("massage_list")
    return {"message": "Massage updated", "data": massage.__dict__}
