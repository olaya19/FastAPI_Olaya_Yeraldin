from app.auth.auth_handler import create_access_token
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(data: LoginRequest):
    # Usuario y password fijos de ejemplo
    if data.username == "admin" and data.password == "admin":
        token = create_access_token({"sub": data.username})
        return {"access_token": token, "token_type": "bearer"}
    return {"error": "Credenciales inválidas"}
