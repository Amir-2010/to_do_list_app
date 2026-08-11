
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
from config import setting # setting is sql_address

engine = create_engine(setting)
local_session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()