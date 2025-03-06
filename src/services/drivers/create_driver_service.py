from typing import Optional

from models.drivers.select_driver_by_cpf import select_driver
from models.drivers.insert_driver import add_driver
from errors.drivers.driver_already_exists import DriverAlreadyExistsError
from errors.global_error import GlobalError

def create(name: str, cpf: str, registration: Optional[str], phone: str):
    driver_exists = select_driver(cpf)

    if driver_exists:
        raise DriverAlreadyExistsError("Ja existe um motorista cadastrado com este cpf.")
    
    try:
        add_driver(name=name, cpf=cpf, registration=registration, phone=phone)
    except:
        raise GlobalError("Não foi possível cadastrar um novo motorista, tente novamente mais tarde!")