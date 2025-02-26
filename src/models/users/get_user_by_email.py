from utils.session import session
from sqlalchemy import Select

from models.table_models import User

def get_user_by_email(email: str):
    with session:
        query = Select(User).where(User.email == email)

        user = session.scalars(query).first()

        return user