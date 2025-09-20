# tests/test_{TU_PREFIJO}.py
import pytest
from fastapi.testclient import TestClient

class TestLavanderiaAPI:
    
    ##Tests específicos para {TU_DOMINIO} - FICHA 3147246
    ##🚨 PERSONALIZAR TODO SEGÚN TU NEGOCIO
    

    def test_create_pedido_success(self, client, sample_pedido_data, auth_headers):
        ###Test de creación exitosa de pedido en lavanderia
        response = client.post(
            ###f\"/{tu_prefijo}{tu_entidad}s/\",
            json=sample_pedido_data,
            headers=auth_headers
        )

        assert response.status_code == 201
        data = response.json()

        # Validaciones específicas de tu dominio
        assert data["cliente"] == sample_pedido_data["cliente"]
        assert data["prendas"] == sample_pedido_data["prendas"]
        # Agregar más validaciones específicas

    def test_get_pedido_not_found(self, client, auth_headers):
        ##"Test de pedido no encontrado en Lavanderia
        response = client.get("laundry_pedidos/999", headers=auth_headers)

        assert response.status_code == 404
        assert "pedido no encontrado" in response.json()["detail"]

    def test_pedido_validation_error(self, client, auth_headers):

        # Datos inválidos específicos de tu pedido
        invalid_data = {
            "cliente":" ",
            "prendas":"-3",
            "tipo_servicio":"Lavado rápido"

        }

        response = client.post(
            "/laundry_pedidos/",
            json=invalid_data,
            headers=auth_headers
        )

        assert response.status_code == 422
        errors = response.json()["detail"]

        # Validar errores específicos de tu dominio
        assert any("cliente" in str(error) for error in errors)
        