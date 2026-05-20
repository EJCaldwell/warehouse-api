from pydantic import BaseModel
from models import Item


class CreateItemRequest(BaseModel):
    name: str
    description: str
    weight: int

class CreateItemResponse(BaseModel):
    id: int
