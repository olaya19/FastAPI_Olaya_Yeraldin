Práctica 10: Estructura Básica del Proyecto
🎯 Objetivo Básico
Organizar tu código FastAPI en una estructura simple y profesional en 90 minutos (Bloque final), enfocándose solo en lo esencial para un proyecto limpio.

⏱️ Tiempo: 90 minutos (Bloque final)
📋 Pre-requisitos
✅ Manejo de errores funcionando (Práctica 9 completada)
✅ Todas las prácticas de la Semana 2 completadas
✅ Conocimiento básico de organización de archivos
✅ Energía para el último empujón del bootcamp
🚀 Desarrollo Rápido (Solo 3 pasos)
Paso 1: Estructura Simple del Proyecto (30 min)
Problema: Tu código está todo en un archivo main.py y es difícil de mantener.

Solución: Separar en archivos organizados pero simples.

# Crear estructura básica
mkdir mi-api-organizada
cd mi-api-organizada

# Crear carpetas principales
mkdir models
mkdir routers
mkdir services

# Crear archivos básicos
touch main.py
touch models/__init__.py
touch models/product.py
touch routers/__init__.py
touch routers/products.py
touch services/__init__.py
touch services/product_service.py
Estructura final simple:

mi-api-organizada/
├── main.py                 # Archivo principal
├── models/
│   ├── __init__.py
│   └── product.py          # Modelos Pydantic
├── routers/
│   ├── __init__.py
│   └── products.py         # Endpoints de productos
└── services/
    ├── __init__.py
    └── product_service.py  # Lógica de negocio
1. Crear modelos organizados (models/product.py):

2. Crear servicio de lógica (services/product_service.py):


1. Archivo principal (main.py):


2. Testing básico:

# Ejecutar la API
python main.py

# Probar endpoints
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/products/


1. Testing completo de la estructura:

# Verificar que todos los archivos existen
ls -la mi-api-organizada/
ls -la mi-api-organizada/models/
ls -la mi-api-organizada/routers/
ls -la mi-api-organizada/services/

# Ejecutar la API
cd mi-api-organizada
python main.py

3. Verificar documentación automática:

💻 Ejemplos Prácticos
Estructura Final:
mi-api-organizada/
├── main.py                    # 🚀 Aplicación principal
├── models/
│   ├── __init__.py
│   └── product.py            # 📦 Modelos Pydantic
├── routers/
│   ├── __init__.py
│   └── products.py           # 🛣️ Endpoints REST
└── services/
    ├── __init__.py
    └── product_service.py     # 🔧 Lógica de negocio
¿Qué lograste?
✅ Separación de responsabilidades: Cada archivo tiene una función específica
✅ Código organizado: Fácil de mantener y escalar
✅ Estructura profesional: Siguiendo mejores prácticas
✅ API funcional: Con todos los endpoints CRUD
✅ Documentación automática: Swagger y ReDoc incluidos

✅ Entregables
Al finalizar esta práctica deberías tener:

✅ Estructura de proyecto profesional completamente organizada
✅ Separación clara de responsabilidades entre modelos, servicios y routers
✅ API funcional con todos los endpoints CRUD
✅ Código mantenible y fácil de escalar
✅ Documentación automática con Swagger UI
Comandos de Testing Final
# Ejecutar la API estructurada
cd mi-api-organizada
python main.py

# Testing de endpoints
curl -X GET "http://localhost:8000/health"
curl -X GET "http://localhost:8000/api/v1/products/"

# Documentación automática
# http://localhost:8000/docs
# http://localhost:8000/redoc
Práctica desarrollada para Semana 3 - Bootcamp FastAPI
Tiempo estimado: 90 minutos