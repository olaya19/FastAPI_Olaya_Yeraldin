# 📄 3 docs/quality_standards.md

(estándares de calidad aplicados)
[Empieza aquí y termina donde dice --- END quality_standards.md ---]*

# Quality Standards — TravelExplorer

Herramientas de calidad y configuración.

---

## Herramientas
- **Black**: formateo automático (88 chars).
- **isort**: ordena imports (perfil black).
- **flake8**: linting PEP8.
- **pre-commit**: hooks (black + isort + flake8).
- **pytest + coverage**: tests y métricas.
- **GitHub Actions**: CI que ejecuta lint + tests.

## Comandos
Formatear:
```bash
black app tests
isort app tests


Lint:

flake8 app tests


CI local completo:

./scripts/quality.sh

Umbrales

Coverage mínimo: 80 % (actual 93 %).

flake8: 0 errores críticos.

Checklist antes de entregar

 black y isort sin cambios pendientes

 flake8 sin errores

 pytest pasa y coverage ≥80 %

 pre-commit instalado y funcionando

--- END quality_standards.md ---