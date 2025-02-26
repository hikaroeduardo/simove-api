from fastapi import HTTPException, status

from utils.session import session
from models.table_models import User

def add_user(name: str, email: str, password: str, phone: str, id_superitendence: int):
    
    new_user = User(name=name, email=email, password=password, phone=phone, id_superitendence=id_superitendence)

    with session:
        try:
            session.add(new_user)
            session.commit()
        except:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Não foi possível criar um novo usuário, tente novamente mais tarde."
            )