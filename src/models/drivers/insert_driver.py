from typing import Optional

from models.table_models import Driver
from utils.session import session

def add_driver(name: str, cpf: str, registration: Optional[str], phone: str):
    with session:
        driver = Driver(name=name, cpf=cpf, registration=registration, phone=phone)

        session.add(driver)
        session.commit()