from errors.global_error import GlobalError
from models.vehicles.select_all_vehicles import select_vehicles

def get_vehicles():
    try:
        vehicles = select_vehicles()

        return vehicles
    except:
        raise GlobalError("Não foi possível buscar dados dos veículos, tente novamente mais tarde!")