from utils.session import session

from models.table_models import Request

def create_request(id_user: int, id_superitendence: int, departure_location: str, destination_location: str, number_peoples: int):
    with session:
        request = Request(id_user=id_user, id_superitendence=id_superitendence, departure_location=departure_location, destination_location=destination_location, number_peoples=number_peoples)

        session.add(request)
        session.commit()