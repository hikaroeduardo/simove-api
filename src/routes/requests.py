from fastapi import APIRouter

from controllers.requests.create_request_controller import create_request_controller

request_routes = APIRouter(tags=["Requests"])

request_routes.post('/request')(create_request_controller)