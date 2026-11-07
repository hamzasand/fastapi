from pydantic import BaseModel, Field

class Supplier(BaseModel):
    name: str
    email: str
    country: str = "PK"

class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    supplier: Supplier
    tags: list[str]= []

example = ProductCreate(
    name="Wireless Mouse",
    price=18.99,
    stock=42,
    supplier={"name": "M.Hamza", "email": "mhamza@gmail.pk"},
    tags=["mouse", "wireless"],
)
print(example.model_dump())
