from fastapi import APIRouter

from controllers.drivers.create_driver_controller import create_driver

driver_routes = APIRouter(tags=["Drivers"])

driver_routes.post('/driver')(create_driver)