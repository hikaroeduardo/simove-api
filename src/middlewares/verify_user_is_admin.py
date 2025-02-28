from fastapi import Depends, HTTPException, status

from middlewares.verify_user_is_logged import user_is_logged
from models.users.select_user_by_id import select_user_by_id

def user_is_admin(id_user: int = (Depends(user_is_logged))):
    user = select_user_by_id(str(id_user))

    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Este usuário não tem permissão para executar esta funcionalidade."
        )
    
    return str(id_user)