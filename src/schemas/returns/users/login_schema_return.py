from pydantic import BaseModel

class LoginReturn(BaseModel):
    token: str