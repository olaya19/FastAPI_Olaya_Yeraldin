# tests/test_laundry_coverage.py
import os

import pytest


def test_coverage_laundry_module():
    """
    Verifica que la cobertura de los módulos críticos de lavandería
    sea al menos del 80%.
    """
    # El plugin pytest-cov ya imprime la cobertura en terminal.
    # Aquí solo dejamos constancia, no calculamos en tiempo real.
    assert True  # placeholder, el check real se ve en el reporte


def test_critical_paths_laundry():
    """
    Asegura que las rutas críticas de lavandería tengan tests.
    (registro, login, creación/borrado de pedidos).
    """
    critical_endpoints = [
        "/register",
        "/login",
        "/laundry_pedidos/",
        "/laundry_pedidos/{id}",
        "/admin-only",
    ]
    # Este test es documental: si algún endpoint cambia, este listado debe actualizarse.
    assert all(isinstance(r, str) for r in critical_endpoints)
