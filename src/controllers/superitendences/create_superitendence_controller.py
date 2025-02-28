from fastapi import status, HTTPException, Depends
from fastapi.responses import JSONResponse

from errors.superitendences.superitendence_name_already_exists import SuperitendenceNameAlreadyExists
from errors.superitendences.superitendence_acronym_already_exists import SuperitendenceAcronymAlreadyExists
from middlewares.verify_user_is_admin import user_is_admin
from schemas.create_superitendence_schema import CreateSuperitendenceSchema
from services.superitendences.create_superitendence_service import create

async def create_superitendence(data_superitendence: CreateSuperitendenceSchema, id_user: str = Depends(user_is_admin)):
    try:
        create(name=data_superitendence.name, acronym=data_superitendence.acronym)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "success": "Superitendência cadastrada com sucesso!"
            }
        )
    except SuperitendenceNameAlreadyExists as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
    except SuperitendenceAcronymAlreadyExists as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Não foi possível cadastrar uma nova superitendência, tente novamente mais tarde!"
        )