
from pydantic_settings import BaseSettings

class settings(BaseSettings):
    sql_address:str = "sqlite:///D:/work projects/to_do_list_app/app/database.db"

setting_obj = settings()