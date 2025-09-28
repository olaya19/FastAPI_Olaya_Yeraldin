from datetime import datetime

from pydantic import BaseModel


# Modelo simple en memoria para representar un viaje
class Viaje(BaseModel):
    id: int
    destino: str
    fecha_salida: datetime
    fecha_regreso: datetime
    cupo: int
