from datetime import datetime, timedelta

from app.utils.helpers import validar_fechas


def test_validar_fechas():
    salida = datetime.utcnow()
    regreso = salida + timedelta(days=1)
    assert validar_fechas(salida, regreso) is True
