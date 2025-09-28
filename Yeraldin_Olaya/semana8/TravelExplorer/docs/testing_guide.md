# 2 docs/testing_guide.md

(guía para correr y entender los tests)
[Empieza aquí y termina donde dice --- END testing_guide.md ---]*

# Testing Guide — TravelExplorer

Cómo correr los tests y verificar cobertura.

---

## Instalación
```bash
pip install -r requirements-dev.txt

Ejecutar todo
pytest --cov=app --cov-report=term-missing --cov-report=html


HTML en htmlcov/index.html.

Ejecutar un archivo
pytest tests/test_tipo_b/test_endpoints.py -q

Fixtures clave

client: TestClient de FastAPI.

auth_headers: JWT de prueba.

viaje_base: datos genéricos de viaje.

Buenas prácticas

Tests aislados.

Cubre casos positivos y negativos.

Verifica en htmlcov las líneas en rojo para aumentar cobertura.

Objetivo

Cobertura mínima exigida: 80 % (actual: ~93 %).

--- END testing_guide.md ---