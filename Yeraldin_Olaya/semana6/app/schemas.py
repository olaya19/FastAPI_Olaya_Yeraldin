from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, validator


# Schemas de Usuario
class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    is_active: bool


# Schemas de Autenticación
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Schemas de Producto
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: int


class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: int
    created_by: int


# Schemas de Favoritos
class FavoriteResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    product: ProductResponse


class PedidoCreate(BaseModel):
    cliente: str = Field(..., min_length=1)
    prendas: int = Field(..., gt=0)
    tipo_servicio: str = Field(..., min_length=3)
    fecha_recepcion: date
    fecha_entrega: date
    estado: Optional[str] = "pendiente"

    @validator("fecha_entrega")
    def entrega_no_menor_recepcion(cls, v, values):
        fr = values.get("fecha_recepcion")
        if fr and v < fr:
            raise ValueError("fecha_entrega debe ser >= fecha_recepcion")
        return v


class PedidoResponse(BaseModel):
    id: int
    cliente: str
    prendas: int
    tipo_servicio: str
    fecha_recepcion: date
    fecha_entrega: date
    estado: str

    class Config:
        orm_mode = True
