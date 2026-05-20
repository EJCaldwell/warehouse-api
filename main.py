from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Session, select        
                                            
from database import get_db                 
from models import Item
from schemas import CreateItemRequest, CreateItemResponse, UpdateItemRequest


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


@app.patch("/item/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_item(item_id: int, update_request: UpdateItemRequest, db: Session = Depends(get_db)) -> None:
    item: Item | None = db.get(Item, item_id)

    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id {item_id} not found")

    if update_request.name is not None:
        item.name = update_request.name

    if update_request.description is not None:
        item.description = update_request.description

    if update_request.weight is not None:
        item.weight = update_request.weight

    db.commit()


@app.delete("/item/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int, db: Session = Depends(get_db)) -> None:
    item: Item | None = db.get(Item, item_id)

    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID {item_id} was not found")

    db.delete(item)
    db.commit()
