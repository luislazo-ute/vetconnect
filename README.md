# VetConnect — Backend API REST (Django + DRF + PostgreSQL + MongoDB)

API REST para la gestión de una clínica veterinaria: clientes, mascotas, veterinarios, citas, historial clínico, **facturación e inventario**, **hospitalización, vacunas y recetas**, más 5 colecciones MongoDB para datos de sensores y multimedia (telemedicina, monitoreo de signos, dictado por voz, tracking de visitas y galería).

## Integrantes
- **Luis Lazo** — Setup del proyecto, núcleo `pacientes`, MongoDB, despliegue y CI/CD.
- **Kevin** — App `facturacion` (servicios, facturas, pagos, inventario, compras).
- **Johan** — App `clinica` (vacunas, habitaciones, hospitalización, recetas, notificaciones).

## Descripción del sistema
Arquitectura híbrida (persistencia políglota):
- **PostgreSQL (20 tablas)** para el núcleo transaccional con integridad referencial.
- **MongoDB (5 colecciones)** para datos de sensores/multimedia de alto volumen (extra del equipo).
- Autenticación **JWT** (`djangorestframework-simplejwt`) con rotación y blacklist.
- Documentación **OpenAPI/Swagger** con `drf-spectacular`.
- Despliegue en **VPS** con Gunicorn + Nginx + HTTPS (Let's Encrypt) y **CI/CD** con GitHub Actions.

### URL pública
- API: `https://vetconnect-api.uaeftt-ute.site/api/`
- **Documentación Swagger: `https://vetconnect-api.uaeftt-ute.site/api/docs/`**
- Redoc: `https://vetconnect-api.uaeftt-ute.site/api/redoc/`
- Admin: `https://vetconnect-api.uaeftt-ute.site/admin/`

---

## Las 20 tablas PostgreSQL
**pacientes (5):** `cliente`, `veterinario`, `mascota`, `cita`, `historial_medico`
**facturacion (9):** `servicio`, `factura`, `detalle_factura`, `pago`, `categoria_producto`, `producto`, `proveedor`, `compra`, `detalle_compra`
**clinica (6):** `vacuna`, `habitacion`, `hospitalizacion`, `receta`, `detalle_receta`, `notificacion`

**Tipos de relación**
- **One-to-One:** `cliente.user → User`, `veterinario.user → User`.
- **One-to-Many:** la mayoría (ej. `mascota → cliente`, `factura → cliente`, `cita → mascota/veterinario`).
- **Many-to-Many (con tabla intermedia):** `factura ↔ servicio` vía `detalle_factura`, `compra ↔ producto` vía `detalle_compra`, `receta ↔ producto` vía `detalle_receta`.

### MongoDB (5 colecciones — extra)
`consultas_remotas`, `monitoreo_signos`, `notas_voz_consulta`, `tracking_visitas`, `galeria_mascota`.

---

## Instalación (local)

```bash
# 1. Clonar
git clone https://github.com/luislazo-ute/vetconnect.git
cd vetconnect

# 2. Entorno virtual (uv)
uv venv --python 3.12
uv pip install -r requirements.txt

# 3. Variables de entorno
cp .env.example .env
# edita .env con tus credenciales (ver abajo)

# 4. Migraciones
.venv/bin/python manage.py migrate

# 5. Superusuario
.venv/bin/python manage.py createsuperuser

# 6. Servidor de desarrollo
.venv/bin/python manage.py runserver
```

### Variables de entorno (`.env`)
```ini
SECRET_KEY=tu-clave-secreta
DEBUG=True

DB_NAME=vetconnect_db
DB_USER=vetuser
DB_PASSWORD=vet123456
DB_HOST=localhost
DB_PORT=5432

MONGO_URI=mongodb://localhost:27017/
MONGO_DB=vetconnect_mongo

CORS_ALLOW_ALL_ORIGINS=True

# Solo para correr los tests (rol de Postgres con permiso CREATEDB)
DB_TEST_USER=postgres
DB_TEST_PASSWORD=tu-password
```

### Base de datos PostgreSQL
```sql
CREATE USER vetuser WITH PASSWORD 'vet123456';
CREATE DATABASE vetconnect_db OWNER vetuser;
GRANT ALL PRIVILEGES ON DATABASE vetconnect_db TO vetuser;
```

### Tests
```bash
.venv/bin/python manage.py test     # requiere PostgreSQL y MongoDB corriendo
```

---

## Despliegue (VPS Ubuntu)
Resumen (procedimiento completo paso a paso en el historial del proyecto):
1. Instalar Python 3.12 (uv), PostgreSQL y MongoDB.
2. Clonar en `/opt/vetconnect`, `uv venv` + `uv pip install -r requirements.txt`.
3. Crear `.env` de producción (`DEBUG=False`).
4. `migrate`, `createsuperuser`, `collectstatic`.
5. **Gunicorn** como servicio systemd (socket Unix).
6. **Nginx** como proxy inverso + archivos estáticos.
7. **HTTPS** con Certbot (Let's Encrypt).
8. **CI/CD** con GitHub Actions: en cada push a `main` corre los tests (Postgres+Mongo) y, si pasan, redespliega por SSH.

---

## Uso de la API

### 1. Registro
```bash
curl -X POST https://vetconnect-api.uaeftt-ute.site/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"ana","email":"ana@vet.com","password":"ClaveSegura123","password2":"ClaveSegura123"}'
```

### 2. Login (obtener token JWT)
```bash
curl -X POST https://vetconnect-api.uaeftt-ute.site/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"ana","password":"ClaveSegura123"}'
# → {"access":"...","refresh":"...","user":{...}}
```

### 3. Usar un endpoint protegido
```bash
curl https://vetconnect-api.uaeftt-ute.site/api/mascotas/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

### 4. Búsqueda, filtros, orden y paginación
```
GET /api/mascotas/?search=Firulais
GET /api/mascotas/?especie=perro&is_active=true
GET /api/mascotas/?ordering=nombre
GET /api/mascotas/?page=2&page_size=20
```

### Roles
- **Usuario** (autenticado): puede **leer** (GET) los recursos.
- **Administrador** (`is_staff`): puede **crear / actualizar / eliminar** y **gestionar usuarios**.

---

## Endpoints

### Autenticación
| Método | Ruta | Descripción |
|---|---|---|
| POST | `/api/auth/register/` | Registro (devuelve tokens) |
| POST | `/api/auth/login/` (= `/api/token/`) | Login JWT |
| POST | `/api/token/refresh/` | Renovar access token |
| POST | `/api/token/verify/` | Verificar token |
| POST | `/api/auth/logout/` | Logout (blacklist del refresh) |

### Usuarios
| Método | Ruta |
|---|---|
| GET/POST | `/api/users/` (solo admin) |
| GET/PATCH | `/api/users/profile/` |
| POST | `/api/users/change-password/` |

### Recursos CRUD (`GET, POST, PUT, PATCH, DELETE`)
**Pacientes:** `/api/clientes/`, `/api/veterinarios/`, `/api/mascotas/`, `/api/citas/`, `/api/historiales/`
**Facturación:** `/api/servicios/`, `/api/facturas/`, `/api/detalles-factura/`, `/api/pagos/`, `/api/categorias-producto/`, `/api/productos/`, `/api/proveedores/`, `/api/compras/`, `/api/detalles-compra/`
**Clínica:** `/api/vacunas/`, `/api/habitaciones/`, `/api/hospitalizaciones/`, `/api/recetas/`, `/api/detalles-receta/`, `/api/notificaciones/`

### MongoDB
`/api/mongo/consultas/`, `/api/mongo/monitoreo/`, `/api/mongo/notas-voz/`, `/api/mongo/tracking/`, `/api/mongo/galeria-mascota/` (cada una con detalle `/<id>/`)

### Utilidad / Docs
| Ruta | Descripción |
|---|---|
| `/api/health/` | Health check (público) |
| `/api/docs/` | **Swagger UI** |
| `/api/redoc/` | Redoc |
| `/api/schema/` | Esquema OpenAPI |

---

## Stack
Django 6 · Django REST Framework · djangorestframework-simplejwt · django-filter · drf-spectacular · PostgreSQL (psycopg2) · MongoDB (pymongo) · django-environ · Gunicorn · Nginx.
