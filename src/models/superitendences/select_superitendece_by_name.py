from sqlalchemy import select

from models.table_models import Superitendence
from utils.session import session

def select_superitendence(name: str):
    with session:
        query = select(Superitendence.name, Superitendence.acronym).where(Superitendence.name == name)

        superitendence = session.execute(query).mappings().first()

        return superitendence