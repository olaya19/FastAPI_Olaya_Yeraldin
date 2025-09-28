from app.routers import auth_routes, tipo_b_routes  # <-- IMPORTA AMBOS ROUTERS
from fastapi import FastAPI

# Instancia principal de la aplicación FastAPI
app = FastAPI(
    title="TravelExplorer API",
    description=(
        "API de Agencia de Viajes (Tipo B) con " "Programación Temporal y Auth JWT"
    ),
    version="1.0.0",
)

# Rutas principales
app.include_router(auth_routes.router)  # Endpoints de autenticación
app.include_router(tipo_b_routes.router)  # Endpoints CRUD de viajes


# Ruta raíz de bienvenida
@app.get("/")
def root():
    return {"message": "Bienvenido a TravelExplorer API"}
