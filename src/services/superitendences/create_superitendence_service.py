from sqlalchemy.exc import IntegrityError

from errors.superitendences.superitendence_name_already_exists import SuperitendenceNameAlreadyExists
from errors.superitendences.superitendence_acronym_already_exists import SuperitendenceAcronymAlreadyExists
from models.superitendences.select_superitendece_by_name import select_superitendence
from models.superitendences.insert_new_superitendence import insert_superitendence

def create(name: str, acronym: str):
    superitendence = select_superitendence(name)

    if superitendence:
        raise SuperitendenceNameAlreadyExists("ja existe uma superintendência com este nome em nosso sistema! Por favor, insira um nome diferente.")
    
    try:
        insert_superitendence(name, acronym)
    except IntegrityError:
        raise SuperitendenceAcronymAlreadyExists("ja existe uma superintendência com esta sigla em nosso sistema! Por favor, insira uma sigla diferente.")