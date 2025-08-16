# Mi API FastAPI - Semana 2

## ¿Qué hace?

API mejorada con validación automática de datos y type hints.

## Nuevos Features (Semana 2)

- ✅ Type hints en todas las funciones
- ✅ Validación automática con Pydantic
- ✅ Endpoint POST para crear datos
- ✅ Parámetros de ruta (ejemplo: /products/{id})
- ✅ Búsqueda con parámetros query

## ¿Cómo ejecutar?

pip install fastapi pydantic uvicorn
uvicorn main:app --reload

## Endpoints principales
GET /: Mensaje de bienvenida
POST /products: Crear nuevo producto
GET /products: Ver todos los productos
GET /products/{id}: Ver producto específico
GET /search?name=...: Buscar productos

## Reflexión
Los type hints, junto con la validación automática de FastAPI, hacen que nuestra API sea más segura y fácil de usar, al garantizar que los datos que recibe cumplen con los tipos esperados. Esto mejora la claridad del código y reduce errores, facilitando tanto el desarrollo como el mantenimiento de la aplicación.
