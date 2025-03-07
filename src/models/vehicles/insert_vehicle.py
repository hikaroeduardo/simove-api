from models.table_models import Vehicle
from utils.session import session

def add_vehicle(model: str, brand: str, plate: str, year: str, color: str, id_fuel: int, renavam: str):
    with session:
        vehicle = Vehicle(model=model, brand=brand, plate=plate, year=year, color=color, id_fuel=id_fuel, renavam=renavam)

        session.add(vehicle)
        session.commit()