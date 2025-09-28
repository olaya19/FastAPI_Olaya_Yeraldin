import redis.asyncio as aioredis


async def send_alert(message: str):
    try:
        r = aioredis.from_url("redis://localhost:6379")
        await r.publish("alerts_channel", message)
    except Exception as e:
        print("No se pudo enviar alerta:", e)
