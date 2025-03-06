from fastapi import APIRouter

from controllers.drivers.create_driver_controller import create_driver

driver_routes = APIRouter(tags=["Drivers"])

driver_routes.post('/driver', responses={
    201: {
        "description": "CREATED",
        "content": {
            "application/json": {
                "example": {"success": "Motorista cadastrado com sucesso!"}
            }
        }
    },
    400: {
        "description": "BAD REQUEST",
        "content": {
            "application/json": {
                "example": {"detail": "Ja existe um motorista cadastrado com este cpf."}
            }
        }
    },
    500: {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Não foi possível cadastrar um novo motorista, tente novamente mais tarde!"}
            }
        }
    },
}, status_code=201)(create_driver)