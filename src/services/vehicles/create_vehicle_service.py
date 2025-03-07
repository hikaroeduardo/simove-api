from models.vehicles.select_vehicle_by_plate import select_vehicle
from models.vehicles.insert_vehicle import add_vehicle
from errors.vehicles.vehicle_already_exists import VehicleAlreadyExistsError
from errors.global_error import GlobalError

def create(model: str, brand: str, plate: str, year: str, color: str, id_fuel: int, renavam: str):
    vehicle_exists = select_vehicle(plate)

    if vehicle_exists:
        raise VehicleAlreadyExistsError("Ja existe um veículo cadastrado com esta placa.")
    
    try:
        add_vehicle(model=model, brand=brand, plate=plate, year=year, color=color, id_fuel=id_fuel, renavam=renavam)
    except:
        raise GlobalError("Não foi possível cadastrar um novo veículo, tente novamente mais tarde!")