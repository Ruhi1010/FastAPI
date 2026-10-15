from fastapi import FastAPI, HTTPException
from service.products import get_all_products

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI E-commerce application!"}

@app.get("/products")
def get_product():
    return get_all_products()
    
    
