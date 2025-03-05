from fastapi import APIRouter

from controllers.requests.create_request_controller import create_request_controller

request_routes = APIRouter(tags=["Requests"])

request_routes.post('/request', responses={
    201: {
        "description": "CREATED",
        "content": {
            "application/json": {
                "example": {"success": "Solicitação criada com sucesso!"}
            }
        }
    },
    500: {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Não foi possível criar uma nova solicitação, tente novamente mais tarde!"}
            }
        }
    },
}, status_code=201)(create_request_controller)