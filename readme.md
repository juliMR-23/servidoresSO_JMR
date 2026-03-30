# Actividad servidores - SO
**Julián Marín Ramírez**

FastAPI + SQLite + Python

### Características
- API REST con gestión de ítems (columnas id, name, price y created_at)
- Validación Pydantic y soporte para operaciones múltiples (wrappers)
- Gestión de daemons mediante archivos .service en Systemd (WSL/Ubuntu) para automatización y persistencia
- Aislamiento mediante entornos independientes: venv para la API y pipx para JupyterLab

### Exposición de Red (NGROK)
- Túneles HTTPS para publicar los servicios locales
- API: `ngrok http 8000` para acceso a Swagger UI
- Jupyter: `ngrok http 8888` para acceso a IDE remoto (configurado con --ip=0.0.0.0)
- Inspección de tráfico local en tiempo real: `http://127.0.0.1:4040`

### Comandos de Control
- Estado API: `sudo systemctl status items_api.service`
- Estado Jupyter: `sudo systemctl status jupyter.service`
- Prueba local: `http://127.0.0.1:8000/docs`

> Nota: para probar el proyecto se debe crear la base de datos local en `DB_sqlite/datos.db`
