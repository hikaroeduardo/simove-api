from sqlalchemy import select

from models.table_models import Driver
from utils.session import session

def select_drivers():
    with session:
        query = select(Driver.name, Driver.cpf, Driver.registration, Driver.phone)

        drivers = session.execute(query).mappings().all()

        return [dict(driver) for driver in drivers]