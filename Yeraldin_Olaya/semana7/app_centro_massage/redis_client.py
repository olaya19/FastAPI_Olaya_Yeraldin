import redis.asyncio as aioredis

try:
    redis_client = aioredis.from_url("redis://localhost:6379", decode_responses=True)
except Exception as e:
    print("⚠️ No se pudo conectar a Redis:", e)
    redis_client = None
