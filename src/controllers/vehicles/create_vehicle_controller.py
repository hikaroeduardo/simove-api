from fastapi import status, HTTPException, Depends
from fastapi.responses import JSONResponse

from middlewares.verify_user_is_admin import user_is_admin
from schemas.create_vehicles import CreateVehiclesSchema
from services.vehicles.create_vehicle_service import create
from errors.vehicles.vehicle_already_exists import VehicleAlreadyExistsError
from errors.global_error import GlobalError

async def create_vehicle(data_vehicles: CreateVehiclesSchema, id_user: int = Depends(user_is_admin)):
    model = data_vehicles.model
    brand = data_vehicles.brand
    plate = data_vehicles.plate
    year = data_vehicles.year
    color = data_vehicles.color
    id_fuel = data_vehicles.id_fuel
    renavam = data_vehicles.renavam

    try:
        create(model=model, brand=brand, plate=plate, year=year, color=color, id_fuel=id_fuel, renavam=renavam)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": "Veículo cadastrado com sucesso!"
            }
        )
    except VehicleAlreadyExistsError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
    except GlobalError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        )