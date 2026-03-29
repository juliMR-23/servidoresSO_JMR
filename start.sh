#!/bin/bash

# Activar entorno virtual
source venv/bin/activate

# Arrancar el servidor FastAPI
uvicorn api.main:app --host 0.0.0.0 --port 8000