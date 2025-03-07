from fastapi import APIRouter

from controllers.vehicles.create_vehicle_controller import create_vehicle
from controllers.vehicles.list_vehicles_controller import list_vehicles

vehicles_routes = APIRouter(tags=["Vehicles"])

vehicles_routes.post('/vehicle', responses={
    201: {
        "description": "CREATED",
        "content": {
            "application/json": {
                "example": {"success": "Veículo cadastrado com sucesso!"}
            }
        }
    },
    400: {
        "description": "BAD REQUEST",
        "content": {
            "application/json": {
                "example": [
                    {"detail": "Ja existe um veículo cadastrado com esta placa."},
                    {"detail": "Tipo de token inválido. Precisa ser do tipo Bearer."}
                    ]
            }
        }
    },
    403: {
        "description": "FORBIDDEN",
        "content": {
            "application/json": {
                "example": {"detail": "Este usuário não tem permissão para executar esta funcionalidade"}
            }
        }
    },
    500: {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Não foi possível cadastrar um novo veículo, tente novamente mais tarde!"}
            }
        }
    }}, status_code=201)(create_vehicle)

vehicles_routes.get('/vehicles', responses={
    400: {
        "description": "BAD REQUEST",
        "content": {
            "application/json": {
                "example": {"detail": "Tipo de token inválido. Precisa ser do tipo Bearer."}
            }
        }
    },
    403: {
        "description": "FORBIDDEN",
        "content": {
            "application/json": {
                "example": {"detail": "Este usuário não tem permissão para executar esta funcionalidade"}
            }
        }
    },
    500: {
        "description": "INTERNAL SERVER ERROR",
        "content": {
            "application/json": {
                "example": {"detail": "Não foi possível buscar dados dos veículos, tente novamente mais tarde!"}
            }
        }
    }
})(list_vehicles)