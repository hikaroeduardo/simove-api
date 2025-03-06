from sqlalchemy import select

from models.table_models import Driver
from utils.session import session

def select_driver(cpf: str):
    with session:
        query = select(Driver).where(Driver.cpf == cpf)

        driver = session.scalars(query).first()

        return driver