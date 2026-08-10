
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String,Integer,Column
from sqlalchemy.orm import DeclarativeBase

sql_address = "sqlite:///D:/work projects/to_do_list_app/app/database.db"

class Base(DeclarativeBase):
    pass