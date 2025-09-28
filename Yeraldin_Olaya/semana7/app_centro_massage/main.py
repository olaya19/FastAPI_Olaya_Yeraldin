# main.py
from fastapi import FastAPI
import redis.asyncio as aioredis
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from database import Base, engine

# Importar routers
from views import massage_list, massage_create, massage_update, massage_delete

# Importar middleware personalizado
from middleware.logging_middleware import LoggingMiddleware

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Crear app
app = FastAPI(title="Centro Masajes - Semana 7")

# --------------------------
# Middleware Logging
# --------------------------
app.add_middleware(LoggingMiddleware)

# --------------------------
# Configuración Redis Cache
# --------------------------
try:
    redis = aioredis.from_url("redis://localhost:6379", decode_responses=True)
except Exception as e:
    print("⚠️ No se pudo conectar a Redis:", e)
    redis = None

# --------------------------
# Configuración Rate Limiting
# --------------------------
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# --------------------------
# Monitoreo con Prometheus
# --------------------------
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# --------------------------
# Routers
# --------------------------
app.include_router(massage_list.router, prefix="/massages", tags=["list"])
app.include_router(massage_create.router, prefix="/massages", tags=["create"])
app.include_router(massage_update.router, prefix="/massages", tags=["update"])
app.include_router(massage_delete.router, prefix="/massages", tags=["delete"])

# --------------------------
# Endpoint raíz
# --------------------------
@app.get("/")
async def root():
    return {"message": "API Centro Masajes funcionando ✅"}
