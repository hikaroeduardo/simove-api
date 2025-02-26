from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    id_superitendence: int