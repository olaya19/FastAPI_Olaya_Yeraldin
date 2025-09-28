from datetime import datetime


def validar_fechas(salida: datetime, regreso: datetime) -> bool:
    """Devuelve True si la fecha de regreso es posterior a la de salida."""
    return regreso > salida
