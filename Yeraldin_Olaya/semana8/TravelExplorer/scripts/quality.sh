echo ">> Ejecutando formateo, lint y tests..."
./scripts/format.sh
./scripts/lint.sh
pytest
