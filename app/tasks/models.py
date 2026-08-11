
# models is for making a table of data base instead create them in database.py
from sqlalchemy import Column,String,Integer,Boolean
from app.database import Base

class task_models(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String,nullable=False)
    description = Column(String(500),nullable=True)
    work_status = Column(Boolean,default=False)