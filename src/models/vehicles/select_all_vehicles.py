from sqlalchemy import select

from models.table_models import Vehicle
from models.table_models import Fuel
from utils.session import session

def select_vehicles():
    with session:
        query = select(Vehicle.model, Vehicle.brand, Vehicle.plate, Vehicle.year, Vehicle.color, Fuel.name.label("fuel"), Vehicle.renavam).join(Vehicle.fuel)

        vehicles = session.execute(query).mappings().all()

        return [dict(driver) for driver in vehicles]