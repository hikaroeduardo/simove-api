from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse

from middlewares.verify_user_is_admin import user_is_admin
from services.drivers.list_drivers_service import get_drivers
from errors.global_error import GlobalError
from schemas.returns.drivers.list_drivers import ListDriversSchema

async def list_drivers(id_user: int = Depends(user_is_admin)) -> ListDriversSchema:
    try:
        drivers = get_drivers()

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "drivers": drivers
            }
        )
    except GlobalError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        )