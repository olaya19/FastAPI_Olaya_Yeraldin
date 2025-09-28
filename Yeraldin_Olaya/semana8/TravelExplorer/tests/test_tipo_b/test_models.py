from datetime import datetime

from app.models.tipo_b_models import Viaje


def test_viaje_model():
    viaje = Viaje(
        id=99,
        destino="Bogotá",
        fecha_salida=datetime(2025, 12, 1, 10, 0),
        fecha_regreso=datetime(2025, 12, 5, 18, 0),
        cupo=20,
    )
    assert viaje.destino == "Bogotá"
    assert viaje.cupo == 20
    assert viaje.fecha_regreso > viaje.fecha_salida
