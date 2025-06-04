import requests

BASE_URL = "http://127.0.0.1:8000"

def create_product():
    data = {
        "product_id": 1,
        "product_name": "Laptop",
        "product_serial_number": 123456,
        "cost": 75000
    }
    response = requests.post(f"{BASE_URL}/products/", json=data)
    print("CREATE:", response.json())

def get_product(product_id):
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    print("GET:", response.json())

def update_product(product_id):
    data = {
        "product_id": product_id,
        "product_name": "Gaming Laptop",
        "product_serial_number": 999999,
        "cost": 95000
    }
    response = requests.put(f"{BASE_URL}/products/{product_id}", json=data)
    print("UPDATE:", response.json())

def patch_product(product_id):
    data = {
        "cost": 90000
    }
    response = requests.patch(f"{BASE_URL}/products/{product_id}", json=data)
    print("PATCH:", response.json())

def delete_product(product_id):
    response = requests.delete(f"{BASE_URL}/products/{product_id}")
    print("DELETE:", response.json())

if __name__ == "__main__":
    create_product()
    