from fastapi import HTTPException, status

from models.users.select_user_by_id import select_user_by_id
from models.requests.create_request import create_request

def create(departure_location: str, destination: str, number_peoples: int, id_user: int):
    user = select_user_by_id(id_user)

    id_superitendence = user.id_superitendence

    try:
        create_request(number_peoples=number_peoples, departure_location=departure_location, destination_location=destination, id_superitendence=id_superitendence, id_user=id_user)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Não foi possível criar uma nova solicitação, tente novamente mais tarde!"
        )