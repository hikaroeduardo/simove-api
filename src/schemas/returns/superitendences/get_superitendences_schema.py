from pydantic import BaseModel
from typing import List

class DataSuperitendence(BaseModel):
    name: str
    acronym: str

class SuperitendencesSchema(BaseModel):
    superitendences: List[DataSuperitendence]