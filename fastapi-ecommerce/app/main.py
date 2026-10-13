from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI E-commerce application!"}

@app.get("/products/{id}")
def get_product(id: int):
    products = ['Laptop', 'Smartphone', 'Headphones', 'Camera',
                'Smartwatch', 'Tablet', 'Gaming Console', 'Printer', 
                'Monitor', 'Keyboard']
    if id < 0 or id >= len(products):
        raise HTTPException(status_code=404, detail="Product not found")
    return products[id] 
    
