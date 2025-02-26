from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from services.users.create_new_user_service import create
from schemas.create_user_schema import CreateUserSchema

from errors.users.user_already_exists import UserAlreadyExists

async def create_user(user_data: CreateUserSchema):
    try:
        create(user=user_data)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": "Usuário cadastrado com sucesso!"
            }
        )
    except UserAlreadyExists as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )