from typing import Optional
from pydantic import BaseModel

class CreateDriversSchema(BaseModel):
    name: str
    cpf: str
    registration: Optional[str] = None
    phone: str