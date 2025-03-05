import os
from jwt import decode
from jwt.exceptions import InvalidSignatureError
from dotenv import load_dotenv
from fastapi import Header, status, HTTPException
from typing import Annotated

load_dotenv()

def user_is_logged(authorization: Annotated[str, Header()]):
    try:
        if not authorization.startswith('Bearer'):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Tipo de token inválido. Precisa ser do tipo Bearer."
            )

        token = authorization.split()[1]
        secret_key = os.getenv("SECRET_KEY_JWT")
        algorithm = os.getenv("ALGORITHM_JWT")

        token_decode = decode(token, secret_key, algorithm)

        id_user = token_decode.get('id')

        return id_user
    except InvalidSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido."
        )