from pydantic import BaseModel
from datetime import datetime
from typing import List

class ItemCreate(BaseModel):
    name: str
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    created_at: datetime

    class Config:
        from_attributes = True  # para devolver objetos SQLAlchemy

class ItemsRequest(BaseModel):
    items: List[ItemCreate] #porque el POST puede ser de varias filas

# envolver tmb la respuesta, mismo manejo que request
class ItemsResponse(BaseModel):
    items: List[ItemResponse]