from typing import List

from app.auth.dependencies import get_current_user
from app.models.tipo_b_models import Viaje
from app.schemas.tipo_b_schemas import ViajeCreate, ViajeResponse, ViajeUpdate
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/viajes", tags=["Viajes"])
viajes_db: list[Viaje] = []


@router.get("/", response_model=List[ViajeResponse])
def listar_viajes(user: dict = Depends(get_current_user)):
    return viajes_db


@router.post("/", response_model=ViajeResponse, status_code=201)
def crear_viaje(viaje: ViajeCreate, user: dict = Depends(get_current_user)):
    if viaje.fecha_regreso <= viaje.fecha_salida:
        raise HTTPException(
            status_code=400,
            detail="La fecha de regreso debe ser posterior a la de salida",
        )
    if any(v.id == viaje.id for v in viajes_db):
        raise HTTPException(status_code=400, detail="ID de viaje ya existe")
    nuevo = Viaje(**viaje.dict())
    viajes_db.append(nuevo)
    return nuevo


@router.get("/{viaje_id}", response_model=ViajeResponse)
def obtener_viaje(viaje_id: int, user: dict = Depends(get_current_user)):
    for v in viajes_db:
        if v.id == viaje_id:
            return v
    raise HTTPException(status_code=404, detail="Viaje no encontrado")


@router.put("/{viaje_id}", response_model=ViajeResponse)
def actualizar_viaje(
    viaje_id: int, datos: ViajeUpdate, user: dict = Depends(get_current_user)
):
    for v in viajes_db:
        if v.id == viaje_id:
            update_data = datos.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(v, key, value)
            return v
    raise HTTPException(status_code=404, detail="Viaje no encontrado")


@router.delete("/{viaje_id}", status_code=204)
def eliminar_viaje(viaje_id: int, user: dict = Depends(get_current_user)):
    for v in viajes_db:
        if v.id == viaje_id:
            viajes_db.remove(v)
            return
    raise HTTPException(status_code=404, detail="Viaje no encontrado")
