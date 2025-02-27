from fastapi import HTTPException, status

from models.superitendences.get_all_superitendences import get_all_superitendences

def get():
    try:
        superitendences = get_all_superitendences()

        return superitendences
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Não foi possível buscar as superitendências, tente novamente mais tarde."
        )