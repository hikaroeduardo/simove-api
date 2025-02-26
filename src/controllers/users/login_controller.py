from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

from services.users.login_service import get_token
from schemas.login_schema import LoginSchema
from schemas.returns.users.login_schema_return import LoginReturn
from errors.users.incorrect_credentials import IncorrectCredentials

async def login(user_data: LoginSchema) -> LoginReturn:

    try:
        token = get_token(email=user_data.email, password=user_data.password)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "token": token
            }
        )
    except IncorrectCredentials as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error)
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Não foi possível fazer o login, tente novamente mais tarde."
        )