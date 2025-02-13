# Energy API

## Descripción

Este proyecto proporciona una API desarrollada en **FastAPI** para gestionar el consumo e inyección de energía de clientes, incluyendo estadísticas detalladas y datos de carga del sistema.

## Tecnologías utilizadas

- **Lenguaje:** Python 3.12.0
- **Framework:** FastAPI
- **Base de Datos:** PostgreSQL
- **ORM:** SQLAlchemy
- **Gestor de dependencias:** `pip`
- **Entorno Virtual:** `venv`

---

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
 git clone https://github.com/AldairPardo/energy.git
 cd energy
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raiz del proyecto con el siguiente contenido:

```env
DATABASE_URL="postgresql://<USUARIO>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>"
```

### 5. Cargar el esquema de la base de datos

Ejecutar el archivo SQL en PostgreSQL:

```bash
psql -U <USUARIO> -d <DATABASE> -f database_schema.sql
```

### 6. Ejecutar el servidor

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

La API estará disponible en:

- **Documentación interactiva (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Documentación alternativa (ReDoc)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoints principales

### 1. `POST /calculate-invoice`

Calcula la factura para un cliente y un mes específico.

### 2. `GET /client-statistics/{client_id}`

Obtiene las estadísticas de consumo e inyección de energía de un cliente. Incluye:

- Consumo total e inyección en el periodo consultado
- Balance neto de energía (consumo - inyección)
- Histórico por hora

### 3. `GET /system-load`

Obtiene la carga del sistema por hora  basada en los datos de consumo.

### 3. `GET /calculate-concept/{concept}`

Calcula de forma independiente cada concepto de facturación.

---

## Explicación del diseño

La API sigue una arquitectura modular con **FastAPI** para garantizar eficiencia y escalabilidad.

- **Base de datos:** PostgreSQL es utilizada por su confiabilidad en transacciones y escalabilidad.
- **ORM:** SQLAlchemy permite un manejo flexible de la base de datos.
- **Validaciones:** Uso de Helpers para validar entradas.

---

## Mejoras futuras

Algunas optimizaciones y mejoras que pueden implementarse:

- Implementación de caching con Redis para reducir carga en la base de datos.
- Autenticación JWT para mejorar la seguridad en el acceso.
- Implementar pruebas unitarias y de integración.
- Posible separación de endpoints en controllers al crecer la aplicación


