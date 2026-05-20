from pydantic import BaseModel
from models import Item


class CreateItemRequest(BaseModel):
    name: str
    description: str
    weight: float

class CreateItemResponse(BaseModel):
    id: int

class UpdateItemRequest(BaseModel):
    name: str | None = None
    description: str | None = None
    weight: float | None = None
