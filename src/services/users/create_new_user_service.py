import bcrypt
from schemas.create_user_schema import CreateUserSchema
from models.users.get_user_by_email import get_user_by_email
from models.users.add_user import add_user
from errors.users.user_already_exists import UserAlreadyExists

def create(user: CreateUserSchema):
    user_exists = get_user_by_email(user.email)

    if user_exists:
        raise UserAlreadyExists("Este usuário ja existe em nosso sistema.")
    
    password_encode = user.password.encode()
    password_hashed = bcrypt.hashpw(password_encode, bcrypt.gensalt(8)).decode()

    add_user(name=user.name, email=user.email, password=password_hashed, phone=user.phone, id_superitendence=user.id_superitendence)