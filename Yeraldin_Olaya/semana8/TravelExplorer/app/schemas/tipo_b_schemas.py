from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ViajeBase(BaseModel):
    destino: str = Field(..., example="Cartagena")
    fecha_salida: datetime = Field(..., example="2025-12-20T10:00:00")
    fecha_regreso: datetime = Field(..., example="2025-12-25T18:00:00")
    cupo: int = Field(..., example=30)


class ViajeCreate(ViajeBase):
    id: int = Field(..., example=1)


class ViajeUpdate(BaseModel):
    destino: Optional[str] = None
    fecha_salida: Optional[datetime] = None
    fecha_regreso: Optional[datetime] = None
    cupo: Optional[int] = None


class ViajeResponse(ViajeCreate):
    pass
