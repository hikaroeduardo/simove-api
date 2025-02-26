import os
import bcrypt
import jwt
from datetime import datetime, timedelta

from models.users.get_user_by_email import get_user_by_email
from errors.users.incorrect_credentials import IncorrectCredentials

def get_token(email: str, password: str):
    user = get_user_by_email(email)

    if not user:
        raise IncorrectCredentials("E-mail ou senha inválidos.")
        
    password_checked = bcrypt.checkpw(password.encode(), user.password.encode())

    if not password_checked:
        raise IncorrectCredentials("E-mail ou senha inválidos.")
    
    exp_time = datetime.now() + timedelta(days=1)
    payload = {"id": user.id, "exp": exp_time}
    secret_key = os.getenv("SECRET_KEY_JWT")
    algorithm = os.getenv("ALGORITHM_JWT")

    token = jwt.encode(payload, secret_key, algorithm)

    return token