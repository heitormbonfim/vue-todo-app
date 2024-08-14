from fastapi import APIRouter
from pydantic import BaseModel

mock_router = APIRouter()


@mock_router.get("/test")
def mock_test():
    return {"error": False, "message": "Mock router is working"}


@mock_router.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {skip, limit}


@mock_router.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@mock_router.post("/items/")
async def create_item(item: Item):
    return item
