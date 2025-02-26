from fastapi import APIRouter

from controllers.users.create_new_user_controller import create_user

user_routes = APIRouter(tags=["Users"])

user_routes.post('/user', responses={
    201: {
        "description": "CREATED",
        "content": {
            "application/json": {
                "example": {"success": "Usuário cadastrado com sucesso!"}
            }
        }
    },
    400: {
        "description": "BAD REQUEST",
        "content": {
            "application/json": {
                "example": {"detail": "Este usuário ja existe em nosso sistema."}
            }
        }
    },
    500: {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Não foi possível criar um novo usuário, tente novamente mais tarde."}
            }
        }
    }
}, status_code=201)(create_user)