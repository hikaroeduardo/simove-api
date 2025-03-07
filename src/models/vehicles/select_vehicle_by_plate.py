from sqlalchemy import select

from models.table_models import Vehicle
from utils.session import session

def select_vehicle(plate: str):
    with session:
        query = select(Vehicle).where(Vehicle.plate == plate)

        vehicle = session.scalars(query).first()

        return vehicle