# tests/test_laundry_auth.py
from datetime import date, timedelta

import pytest
from auth import create_access_token, get_password_hash
from models import User


def create_user_in_db(session, username, password, role):
    """Helper para crear usuario con rol específico en la DB de pruebas y devolver token."""
    hashed = get_password_hash(password)
    user = User(
        username=username,
        email=f"{username}@test.local",
        hashed_password=hashed,
        role=role,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    token = create_access_token({"sub": user.username})
    return user, token


class TestAuthLavanderia:
    def test_register_laundry_user(self, client):
        """Registro básico — debe crear usuario (role por API puede variar)."""
        payload = {
            "username": "usuario_laundry_test",
            "password": "password123",
            "email": "usuario_laundry@test.local"
            # no enviamos role por seguridad (API puede ignorarlo)
        }
        r = client.post("/register", json=payload)
        assert r.status_code in (200, 201)
        body = r.json()
        assert body.get("username") == payload["username"]

    def test_login_laundry_user(self, client):
        """Login funciona y devuelve access_token."""
        reg = {
            "username": "login_laundry_test",
            "password": "password123",
            "email": "login_laundry@test.local",
        }
        client.post("/register", json=reg)
        r = client.post(
            "/login", json={"username": reg["username"], "password": reg["password"]}
        )
        assert r.status_code == 200
        assert "access_token" in r.json()

    def test_create_requires_auth(self, client):
        """Crear pedido sin token debe fallar (401)."""
        data = {
            "cliente": "Anon",
            "prendas": 1,
            "tipo_servicio": "Lavado",
            "fecha_recepcion": date.today().isoformat(),
            "fecha_entrega": (date.today() + timedelta(days=1)).isoformat(),
            "estado": "pendiente",
        }
        r = client.post("/laundry_pedidos/", json=data)
        # Debe dar 401 (No autenticado). Aceptamos 401/403 si la app usa otro código.
        assert r.status_code in (401, 403)

    def test_admin_can_access_admin_only(self, client, session):
        """Un usuario con rol gerente_lavanderia debe poder acceder a /admin-only."""
        _, token = create_user_in_db(
            session, "admin_laundry_test", "admin123", "gerente_lavanderia"
        )
        headers = {"Authorization": f"Bearer {token}"}
        r = client.get("/admin-only", headers=headers)
        assert r.status_code == 200
        assert "Welcome" in r.json().get("message", "") or "Admin" in r.json().get(
            "message", ""
        )

    def test_regular_user_cannot_access_admin_only(self, client):
        """Usuario normal no debe acceder a endpoint admin-only."""
        # Crear usuario normal por el endpoint (role por default)
        client.post(
            "/register",
            json={
                "username": "regular_user",
                "password": "rpass",
                "email": "r@test.local",
            },
        )
        login = client.post(
            "/login", json={"username": "regular_user", "password": "rpass"}
        )
        token = login.json().get("access_token")
        headers = {"Authorization": f"Bearer {token}"}
        r = client.get("/admin-only", headers=headers)
        assert r.status_code in (401, 403)

    def test_admin_can_delete_pedido(self, client, session):
        """Admin puede borrar un pedido (create -> delete -> 404)."""
        _, token = create_user_in_db(
            session, "admin_del_test", "admin123", "gerente_lavanderia"
        )
        headers = {"Authorization": f"Bearer {token}"}
        # crear pedido
        data = {
            "cliente": "DeleteMe",
            "prendas": 2,
            "tipo_servicio": "Lavado",
            "fecha_recepcion": "2025-09-10",
            "fecha_entrega": "2025-09-12",
            "estado": "pendiente",
        }
        create_r = client.post("/laundry_pedidos/", json=data, headers=headers)
        assert create_r.status_code == 201
        pid = create_r.json()["id"]

        del_r = client.delete(f"/laundry_pedidos/{pid}", headers=headers)
        assert del_r.status_code == 200

        get_r = client.get(f"/laundry_pedidos/{pid}", headers=headers)
        assert get_r.status_code == 404

    def test_regular_user_cannot_delete_pedido(self, client, session):
        """Usuario regular no puede borrar pedidos (si la API lo protege con roles)."""
        # Crear admin y un pedido con admin
        _, admin_token = create_user_in_db(
            session, "admin_for_del", "admin123", "gerente_lavanderia"
        )
        admin_headers = {"Authorization": f"Bearer {admin_token}"}
        data = {
            "cliente": "Protected",
            "prendas": 1,
            "tipo_servicio": "Lavado",
            "fecha_recepcion": "2025-09-10",
            "fecha_entrega": "2025-09-12",
            "estado": "pendiente",
        }
        create_r = client.post("/laundry_pedidos/", json=data, headers=admin_headers)
        pid = create_r.json()["id"]

        # Crear usuario regular via register/login
        client.post(
            "/register",
            json={"username": "no_delete", "password": "p", "email": "p@t.local"},
        )
        login = client.post("/login", json={"username": "no_delete", "password": "p"})
        token = login.json().get("access_token")
        headers = {"Authorization": f"Bearer {token}"}

        # Intento de borrado por usuario regular
        del_r = client.delete(f"/laundry_pedidos/{pid}", headers=headers)
        # Si tu API protege DELETE con require_admin, esperamos 401/403. Si devuelve 200, cambia la protección.
        assert del_r.status_code in (401, 403)
