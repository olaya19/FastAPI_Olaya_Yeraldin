import pytest
from app.auth.auth_handler import create_access_token
from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def auth_headers():
    """Encabezados con un token válido para endpoints protegidos."""
    token = create_access_token({"sub": "admin"})
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def viaje_base():
    return {
        "id": 1,
        "destino": "Cartagena",
        "fecha_salida": "2025-12-20T10:00:00",
        "fecha_regreso": "2025-12-25T18:00:00",
        "cupo": 30,
    }
