from sqlalchemy.exc import IntegrityError

from utils.session import session
from models.table_models import Superitendence

def insert_superitendence(name: str, acronym: str):
    with session:
        new_superitendence = Superitendence(name=name, acronym=acronym)

        try:
            session.add(new_superitendence)
            session.commit()
        except IntegrityError as error:
            raise error