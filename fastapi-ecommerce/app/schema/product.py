from pydantic import BaseModel, Field, AnyUrl
from typing import Annotated, Literal, Optional, List
from uuid import UUID
from datetime import datetime


class Product(BaseModel):
    id: UUID
    sku: Annotated[
        str, 
        Field(
            min_length=6, 
            max_length=30, 
            title="SKU", 
            description="Stock Keeping Unit", 
            examples=["XIAO-359GB-001", "REAL-138GB-003"],
            ),
        ]
    name: Annotated[
        str, 
        Field(
            min_length=3,
            max_length=80,
            title="Product Name",
            description="Name of the product",
            examples=["Xiaomi Model Pro", "Realme Model X"],
            ),
    ]
    
    description: Annotated[
        str,
        Field(
            max_length=500,
            description="Description of the product",
            ),
    ]
    
    category: Annotated[
        str,
        Field(
            min_length=3,
            max_length=50,
            description="Category of the product",
            examples=["laptops", "smartphones"],
            ),
    ]
    
    brand: Annotated[
        str,
        Field(
            min_length=2,
            max_length=50,
            description="Brand of the product",
            examples=["Xiaomi", "Realme"],
            ),
    ]
    
    
    price: Annotated[
        float,
        Field(
            gt=0,
            strict=True,
            description="Price of the product",
        )
    ]
    
    currency: Literal["INR"] = "INR"
    
    discount_percent: Annotated[
        int,
        Field(
            ge=0,
            le=100,
            description="Discount percentage on the product",
        )
    ]
    
    stock: Annotated[
        int,
        Field(
            ge=0,
            description="Number of items in stock",
        )
    ]
    
    is_active: Annotated[
        bool,
        Field(
            description="Is product active?"
        )
    ]
    
    rating: Annotated[
        float,
        Field(
            ge=0,
            le=5,
            description="Rating of the product",
        )
    ]
    
    
    tags: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            max_length=10,
            description="Tags associated with the product",
        )
    ]
    
    
    
    image_urls: Annotated[
            List[AnyUrl],
            Field(
                max_length=1,
                description="At least one image URL of the product",
            )
        ]
    
    # dimensions_cm
    # seller
    
    created_at: datetime

