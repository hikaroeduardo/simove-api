from fastapi import Depends, status
from fastapi.responses import JSONResponse

from services.superitendences.get_all_superitendences_service import get
from middlewares.verify_user_is_logged import user_is_logged
from schemas.returns.superitendences.get_superitendences_schema import SuperitendencesSchema

def get_superitendences(id_user: int = Depends(user_is_logged)) -> SuperitendencesSchema:
    superitendences = get()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "superitendences": superitendences
        }
    )