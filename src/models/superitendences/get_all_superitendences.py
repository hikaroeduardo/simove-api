from sqlalchemy import select

from utils.session import session
from models.table_models import Superitendence

def get_all_superitendences():
    with session:
        query = select(Superitendence.name, Superitendence.acronym)

        results = session.execute(query).mappings().all()

        return [dict(superitendence) for superitendence in results]