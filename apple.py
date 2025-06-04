from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()

# Pydantic model (schema)
class Item(BaseModel):
    name: str
    description: Optional[str] = None

# In-memory storage for items (simulating a database)
fake_db = {}

# Create: Add an item to the "database"
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item_id = len(fake_db) + 1
    fake_db[item_id] = item
    return item

# Read: Get all items
@app.get("/items/", response_model=List[Item])
async def read_items():
    return list(fake_db.values())

# Read: Get an item by ID
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = fake_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Update: Update an existing item by ID
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item
    return item

# Delete: Delete an item by ID
@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    item = fake_db.pop(item_id, None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
