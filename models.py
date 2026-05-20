from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    __tablename__ = "item"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    weight: float

