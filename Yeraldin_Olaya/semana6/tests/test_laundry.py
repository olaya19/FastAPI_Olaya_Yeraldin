# tests/test_{TU_PREFIJO}.py
import pytest
from fastapi.testclient import TestClient
from datetime import date, timedelta


class TestLavanderiaAPI:

    def test_create_pedido_complete(self, client, auth_headers):
        data = {
            "cliente": "Carlos López",
            "prendas": 5,
            "tipo_servicio": "Lavado y planchado",
            "fecha_recepcion": (date.today()).isoformat(),
            "fecha_entrega": (date.today() + timedelta(days=2)).isoformat(),
            "estado": "pendiente"
        }
        response = client.post("/laundry_pedidos/", json=data, headers=auth_headers)
        assert response.status_code == 201
        created = response.json()
        assert created["cliente"] == data["cliente"]
        assert "id" in created

    def test_create_pedido_duplicate(self, client, auth_headers):
        data = {
            "cliente": "Cliente D",
            "prendas": 3,
            "tipo_servicio": "Lavado",
            "fecha_recepcion": "2025-09-01",
            "fecha_entrega": "2025-09-03",
            "estado": "pendiente"
        }
        # 1º creación
        r1 = client.post("/laundry_pedidos/", json=data, headers=auth_headers)
        assert r1.status_code == 201

        # 2º creación duplicada
        r2 = client.post("/laundry_pedidos/", json=data, headers=auth_headers)
        assert r2.status_code == 400
        assert "ya existe" in r2.json()["detail"].lower()

    def test_get_pedido_by_id(self, client, auth_headers):
        data = {
            "cliente": "Cliente X",
            "prendas": 2,
            "tipo_servicio": "Solo lavado",
            "fecha_recepcion": "2025-09-05",
            "fecha_entrega": "2025-09-06",
            "estado": "pendiente"
        }
        create = client.post("/laundry_pedidos/", json=data, headers=auth_headers)
        pid = create.json()["id"]

        r = client.get(f"/laundry_pedidos/{pid}", headers=auth_headers)
        assert r.status_code == 200
        assert r.json()["id"] == pid

    def test_get_all_pedidos(self, client, auth_headers):
        r = client.get("/laundry_pedidos/", headers=auth_headers)
        assert r.status_code == 200
        assert isinstance(r.json(), list)

    def test_update_pedido_complete(self, client, auth_headers):
        data = {
            "cliente": "Cliente UP",
            "prendas": 4,
            "tipo_servicio": "Lavado",
            "fecha_recepcion": "2025-09-07",
            "fecha_entrega": "2025-09-09",
            "estado": "pendiente"
        }
        create = client.post("/laundry_pedidos/", json=data, headers=auth_headers)
        pid = create.json()["id"]

        update = {
            "cliente": "Cliente UP Mod",
            "prendas": 6,
            "tipo_servicio": "Lavado y secado",
            "fecha_recepcion": "2025-09-07",
            "fecha_entrega": "2025-09-10",
            "estado": "en progreso"
        }
        r = client.put(f"/laundry_pedidos/{pid}", json=update, headers=auth_headers)
        assert r.status_code == 200
        assert r.json()["prendas"] == 6

    def test_delete_pedido_success(self, client, auth_headers):
        data = {
            "cliente": "Cliente DEL",
            "prendas": 1,
            "tipo_servicio": "Lavado",
            "fecha_recepcion": "2025-09-08",
            "fecha_entrega": "2025-09-09",
            "estado": "pendiente"
        }
        create = client.post("/laundry_pedidos/", json=data, headers=auth_headers)
        pid = create.json()["id"]

        rdel = client.delete(f"/laundry_pedidos/{pid}", headers=auth_headers)
        assert rdel.status_code == 200

        rget = client.get(f"/laundry_pedidos/{pid}", headers=auth_headers)
        assert rget.status_code == 404

    def test_delete_pedido_not_found(self, client, auth_headers):
        r = client.delete("/laundry_pedidos/999999", headers=auth_headers)
        assert r.status_code == 404

    def test_pedido_business_rules(self, client, auth_headers):
        # prendas <= 0 => 422
        invalid = {
            "cliente": "Cliente Bad",
            "prendas": 0,
            "tipo_servicio": "Lavado",
            "fecha_recepcion": "2025-09-09",
            "fecha_entrega": "2025-09-10",
            "estado": "pendiente"
        }
        r = client.post("/laundry_pedidos/", json=invalid, headers=auth_headers)
        assert r.status_code == 422