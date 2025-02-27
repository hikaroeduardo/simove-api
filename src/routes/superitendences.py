from fastapi import APIRouter

from controllers.superitendences.get_all_superitendences_controller import get_superitendences

superitendence_routes = APIRouter(tags=['Superitendences'])

superitendence_routes.get('/superitendences', responses={
    400: {
        "description": "BAD REQUEST",
        "content": {
            "application/json": {
                "example": {"detail": "Tipo de token inválido. Precisa ser do tipo Bearer."}
            }
        }        
    },
    401: {
        "description": "UNAUTHORIZED",
        "content": {
            "application/json": {
                "example": {"detail": "Token inválido."}
            }
        }
    },
    500: {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Não foi possível buscar as superitendências, tente novamente mais tarde."}
            }
        }
    }
})(get_superitendences)