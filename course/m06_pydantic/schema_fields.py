from random import random
from pydantic import BaseModel, Field

def random_warehouse() ->int:
    return random.randint(1,5)

class Product(BaseModel):
    name: str = Field(
        description="Product Title",
        min_length=3,
        max_length=100,
    )

    price: float =Field(
        description="Price in usd dollars",
        gt=0,
        le=1000,
    )

    stock: int =Field(
        description="Units available in warehouse",
        ge=0,
    )
    
    warehouse: int | None = Field(
        description="warehouse code(1-5). random if not provided",
        default_factory= random_warehouse,
    )