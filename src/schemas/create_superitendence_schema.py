from pydantic import BaseModel

class CreateSuperitendenceSchema(BaseModel):
    name: str
    acronym: str