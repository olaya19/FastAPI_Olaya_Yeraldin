# 📄 1 docs/api_documentation.md

(documentación de los endpoints y ejemplos de uso)
[Empieza aquí y termina donde dice --- END api_documentation.md ---]*

# API Documentation — TravelExplorer

API para gestionar viajes (Tipo B: programación temporal).  
Autenticación: **JWT Bearer** (rutas protegidas).

---

## Endpoints principales

### 1. Autenticación
**POST /auth/login**  
Request:
```json
{ "username": "admin", "password": "admin" }


Response 200:

{ "access_token": "<JWT>", "token_type": "bearer" }


Usar Authorization: Bearer <JWT> en las rutas protegidas.

2. Listar viajes

GET /viajes/ – protegido
Response 200:

[
  {
    "id": 1,
    "destino": "Cartagena",
    "fecha_salida": "2025-12-20T10:00:00",
    "fecha_regreso": "2025-12-25T18:00:00",
    "cupo": 30
  }
]

3. Crear viaje

POST /viajes/ – protegido
Request:

{
  "id": 2,
  "destino": "Medellín",
  "fecha_salida": "2025-11-10T09:00:00",
  "fecha_regreso": "2025-11-15T20:00:00",
  "cupo": 25
}


Responses:

201 Created → viaje creado

400 Bad Request → validación fallida

4. Obtener viaje

GET /viajes/{viaje_id} – protegido
200 OK → retorna viaje • 404 → no existe.

5. Actualizar viaje

PUT /viajes/{viaje_id} – protegido
Request parcial válido (destino, fecha_salida, etc.).
200 OK o 404 si no existe.

6. Eliminar viaje

DELETE /viajes/{viaje_id} – protegido
204 No Content o 404 si no existe.

Swagger

Inicia: uvicorn app.main:app --reload

Abre: http://localhost:8000/docs

Haz login, copia el token y usa Authorize.

Errores comunes

400 Fechas inválidas o id duplicado

401 Token inválido o ausente

404 Recurso no encontrado

--- END api_documentation.md ---