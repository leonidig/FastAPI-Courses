from pydantic import BaseModel, ConfigDict



class ItemSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    price: int
    amount: int
