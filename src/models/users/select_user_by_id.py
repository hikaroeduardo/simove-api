from sqlalchemy import select

from utils.session import session
from models.table_models import User

def select_user_by_id(id: str):
    with session:
        query = select(User).where(User.id == id)

        user = session.scalars(query).first()

        return user

        