import databases
from sqlalchemy.ext.declarative import declarative_base

from app.config import config


def get_db() -> databases.Database:
    database_url = config.DATABASE_URL
    return databases.Database(database_url)


database = get_db()
Base = declarative_base()
metadata = Base.metadata
