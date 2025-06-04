from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users_db = {}


class Product(BaseModel):
    product_id: int
    product_name: str
    product_serial_number: int
    cost: int
   

@app.post("/products/", status_code=201)
def create_product(product: Product):
    users_db[product.product_id] = product
    return {"message": "Product created successfully", "product": product}


@app.get("/products/{product_id}")
def get_product(product_id: int):
    return users_db.get(product_id, "Product not found")


@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    users_db[product_id] = updated_product
    return {"message": "Product updated successfully", "product": updated_product}


@app.patch("/products/{product_id}")
def patch_product(product_id: int, updated_data: dict):
    product = users_db.get(product_id)
    if product:
        for key, value in updated_data.items():
            setattr(product, key, value)
        return {"message": "Product updated successfully", "product": product}
    return {"message": "Product not found"}


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    users_db.pop(product_id, None)
    return {"message": "Product deleted successfully"}