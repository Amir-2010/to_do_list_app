
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
from app.config import setting_obj # setting is sql_address

engine = create_engine(setting_obj.sql_address)
local_session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()