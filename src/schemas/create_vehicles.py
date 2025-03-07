from typing import Optional
from pydantic import BaseModel

class CreateVehiclesSchema(BaseModel):
    model: str
    brand: str
    plate: str
    year: str
    color: str
    id_fuel: int
    renavam: str