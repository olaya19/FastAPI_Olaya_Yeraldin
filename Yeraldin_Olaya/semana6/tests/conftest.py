# tests/conftest.py
import pytest
from database import Base
from fastapi.testclient import TestClient
from main import app, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Base de datos de prueba
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_laundry.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def session(db):
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


# FIXTURE ESPECÍFICA PARA TU DOMINIO
@pytest.fixture
def sample_pedido_data():
    return {
        "cliente": "Carlos López",
        "prendas": 5,
        "tipo_servicio": "Lavado y planchado",
        "fecha_recepcion": "2025-09-13",
        "fecha_entrega": "2025-09-15",
        "estado": "pendiente",
    }


@pytest.fixture
def auth_headers(client):
    # Registrar usuario admin de prueba
    r1 = client.post(
        "/register",
        json={
            "username": "admin_laundry",
            "password": "test123",
            "email": "admin@laundry.test",
            "role": "admin",
        },
    )
    print("REGISTER:", r1.status_code, r1.json())  # 👈 DEPURAR

    # Iniciar sesión
    r2 = client.post(
        "/login", json={"username": "admin_laundry", "password": "test123"}
    )
    print("LOGIN:", r2.status_code, r2.json())  # 👈 DEPURAR

    token = r2.json().get("access_token")
    return {"Authorization": f"Bearer {token}"}

    ###@pytest.fixture
    ### \"\"\"Headers de autenticación para tests\"\"\"
    # Crear usuario de prueba específico para tu dominio
    ##response = client.post(\"/auth/register\", json={
    ##  \"username\": \"admin_{tu_prefijo}\",
    ## \"password\": \"test123\",
    ## \"role\": \"admin\"  # Rol específico de tu dominio
    ##})

    l  ##ogin_response = client.post(\"/auth/login\", data={
    ##  \"username\": \"admin_{tu_prefijo}\",
    ## \"password\": \"test123\"
    ##})
    ##token = login_response.json()[\"access_token\"]
    ##return {\"Authorization\": f\"Bearer {token}\"}
