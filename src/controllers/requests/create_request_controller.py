from fastapi.responses import JSONResponse
from fastapi import Depends, HTTPException, status

from middlewares.verify_user_is_logged import user_is_logged
from schemas.create_request_schema import CreateRequestSchema
from services.requests.create_request_service import create

async def create_request_controller(data_request: CreateRequestSchema, id_user: int = Depends(user_is_logged)):

    departure_location = data_request.departure_location
    destination = data_request.destination_location
    number_peoples = data_request.number_peoples

    try:
        create(departure_location, destination, number_peoples, id_user)

        return JSONResponse(
            content={
                "success": "Solicitação criada com sucesso!"
            }
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Não foi possível criar uma nova solicitação, tente novamente mais tarde!"
        )