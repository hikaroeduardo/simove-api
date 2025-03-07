from pydantic import BaseModel
from typing import List

class VehiclesSchema(BaseModel):
    model: str
    brand: str
    plate: str
    year: str
    color: str
    fuel: str
    renavam: str

class ListVehiclesSchema(BaseModel):
    drivers: List[VehiclesSchema]