from models.database import engine
from sqlalchemy.orm import Session

session = Session(engine)