from errors.global_error import GlobalError
from models.drivers.select_all_drivers import select_drivers

def get_drivers():
    try:
        drivers = select_drivers()

        return drivers
    except:
        raise GlobalError("Não foi possível buscar dados dos motoristas, tente novamente mais tarde!")