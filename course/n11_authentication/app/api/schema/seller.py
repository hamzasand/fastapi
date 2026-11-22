from pydantic import BaseModel, EmailStr

class Baseseller(BaseModel):
    name: str
    email: EmailStr

class SellerCreate(Baseseller):
    password: str

class sellerRead(Baseseller):
    pass