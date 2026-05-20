from fastapi import Depends, FastAPI, status
from sqlmodel import Session, select        
                                            
from database import get_db                 
from models import Item
from schemas import CreateItemRequest, CreateItemResponse


app = FastAPI()


@app.get("/item")
async def get_item(db: Session = Depends(get_db)) -> list[Item]:
    return db.exec(select(Item)).all()


@app.post("/item", status_code=status.HTTP_201_CREATED)
async def create_item(new_item: CreateItemRequest, db: Session = Depends(get_db)) -> CreateItemResponse:
    item = Item(**new_item.model_dump())
    db.add(item)
    db.commit()
    return CreateItemResponse(id=item.id)
