
from pydantic_settings import BaseSettings

class settings(BaseSettings):
    sql_address = "sqlite:///D:/work projects/to_do_list_app/app/database.db"

setting = settings()