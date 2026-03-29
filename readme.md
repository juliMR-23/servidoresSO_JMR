# Actividad servidores - SO
**Julián Marín Ramírez**

FastAPI + SQLite + Python

### Características hasta el momento:
- API con tabla items (id, name, price, created_at)
- Endpoints GET y POST (múltiple con wrappers), validación BaseModel
- Automatización mediante archivo .service en WSL, Ubuntu


Prueba local en interfaz: http://127.0.0.1:8000/docs

sudo systemctl status items_api.service

> Nota: para probar el proyecto se debe crear la base de datos local: `DB_sqlite/datos.db`
