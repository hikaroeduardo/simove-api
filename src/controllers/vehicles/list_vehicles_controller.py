from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse

from middlewares.verify_user_is_admin import user_is_admin
from services.vehicles.list_vehicles_service import get_vehicles
from schemas.returns.vehicles.list_vehicles import ListVehiclesSchema
from errors.global_error import GlobalError

async def list_vehicles(id_user: int = Depends(user_is_admin)) -> ListVehiclesSchema:
    try:
        vehicles = get_vehicles()

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "vehicles": vehicles
            }
        )
    except GlobalError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        )