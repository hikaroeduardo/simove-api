from pydantic import BaseModel
from typing import Optional

class CreateRequestSchema(BaseModel):
    departure_location: str
    destination_location: str
    number_peoples: Optional[int] = 1
