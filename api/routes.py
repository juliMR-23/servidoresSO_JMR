from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from api.database import SessionLocal
from api.models import Item
from api.schemas import ItemsRequest, ItemsResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/items", response_model=ItemsResponse)
def create_items(request: ItemsRequest, db: Session = Depends(get_db)):
    new_items = []
    for item in request.items: #recorre la lista dentro del ItemsRequest (cada item)
        db_item = Item(name=item.name, price=item.price)
        db.add(db_item)
        new_items.append(db_item)

    db.commit() #commit solo una vez al final, guarda todo

    # refresca después para obtener IDs y fechas
    for db_item in new_items:
        db.refresh(db_item)

    # devuelve diccionario con la llave "items"
    return {"items": new_items}

@router.get("/items", response_model=ItemsResponse)
def get_items(db: Session = Depends(get_db)):
    all_items = db.query(Item).all()
    return {"items": all_items} #tamb un diccionario