from pydantic import BaseModel
from typing import List

class DriversSchema(BaseModel):
    name: str
    cpf: str
    registration: str
    phone: str

class ListDriversSchema(BaseModel):
    drivers: List[DriversSchema]