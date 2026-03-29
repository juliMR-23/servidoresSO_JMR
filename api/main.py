from fastapi import FastAPI
from api.routes import router
from api.database import engine, Base
from api.models import Item

#crea la tabla si no existe
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)