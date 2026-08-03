from database.config import Base
from database.config import engine

# Import all models
import database.models


def create_database():
    Base.metadata.create_all(bind=engine)