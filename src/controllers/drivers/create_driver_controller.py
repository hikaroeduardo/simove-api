from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

from schemas.create_drivers import CreateDriversSchema
from services.drivers.create_driver_service import create
from errors.drivers.driver_already_exists import DriverAlreadyExistsError
from errors.global_error import GlobalError

async def create_driver(data_driver: CreateDriversSchema):
    name = data_driver.name
    cpf = data_driver.cpf
    registration = data_driver.registration
    phone = data_driver.phone

    try:
        create(name=name, cpf=cpf, registration=registration, phone=phone)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": "Motorista cadastrado com sucesso!"
            }
        )
    except DriverAlreadyExistsError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
    except GlobalError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        )