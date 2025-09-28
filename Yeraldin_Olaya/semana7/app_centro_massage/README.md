Centro Masajes - Semana 7
# 📚 Descripción del Proyecto

API desarrollada en FastAPI para gestionar un centro de masajes, implementando endpoints CRUD para las sesiones de masaje. El objetivo de la Semana 7 fue explorar técnicas de optimización y monitoreo de APIs con herramientas avanzadas.

## 🗂 Estructura del Proyecto
centro_masajes/
│
├─ models/
│   └─ massage_model.py           # Definición del modelo SQLAlchemy
│
├─ controllers/
│   └─ massage_controller.py      # Funciones de lógica de negocio
│
├─ views/
│   ├─ massage_list.py            # Endpoint GET /massages
│   ├─ massage_create.py          # Endpoint POST /massages
│   ├─ massage_update.py          # Endpoint PUT /massages/{id}
│   └─ massage_delete.py          # Endpoint DELETE /massages/{id}
│
├─ middleware/
│   └─ logging_middleware.py      # Middleware de logging de requests
│
├─ database.py                    # Conexión y configuración de la base de datos
├─ domain.py                      # Configuración de dominio específico
├─ main.py                        # Aplicación principal FastAPI
└─ locustfile.py                  # Pruebas de carga básicas

## ⚙ Tecnologías y Herramientas

FastAPI: Framework principal para la API.
SQLAlchemy: ORM para la base de datos SQLite.
Redis: Cache de datos (opcional).
SlowAPI: Rate limiting de endpoints.
Prometheus + Instrumentator: Monitoreo de métricas básicas.
Middleware Logging: Registro de requests y tiempos de respuesta.
Locust: Pruebas de carga simples.

### Ejecutar la API:

uvicorn main:app --reload


### Ejecutar pruebas de carga básicas:

locust -f locustfile.py
Luego abrir la interfaz web en http://localhost:8089.

### 📝 Endpoints

GET /massages → Listar masajes
POST /massages → Crear sesión de masaje
PUT /massages/{id} → Actualizar sesión
DELETE /massages/{id} → Eliminar sesión
GET / → Endpoint raíz de prueba

### 🔧 Funcionalidades Implementadas

✅ CRUD completo para masajes
✅ Redis cache (conectable a localhost:6379)
✅ Rate limiting con SlowAPI
✅ Middleware de logging de requests
✅ Monitoreo básico con Prometheus
✅ Pruebas de carga con Locust

## 📊 Qué se Aprendió en Semana 7

Configuración y uso de Redis Cache en APIs.
Aplicación de rate limiting para proteger endpoints.
Uso de Prometheus para monitoreo de métricas básicas.
Implementación de middleware de logging para medir tiempos de respuesta.
Ejecución de pruebas de carga simples con Locust.
Buenas prácticas en estructura de proyecto FastAPI y separación de responsabilidades (models/controllers/views).