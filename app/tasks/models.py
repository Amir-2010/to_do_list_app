
# models is for making a table of data base instead create them in database.py
from sqlalchemy import Column,String,Integer,Boolean
from app.database import Base
from sqlalchemy import ForeignKey

class task_models(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    title = Column(String,nullable=False)
    description = Column(String(500),nullable=True)
    work_status = Column(Boolean,default=False)

    def __repr__(self):
        return f"tasks(id={self.id},user id={self.user_id},title={self.title},description={self.description},work status={self.work_status})"

class users_models(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    password = Column(String,nullable=False)
    user_status = Column(Boolean,default=True)

    def __repr__(self):
        return f"users(id={self.id},name={self.name},password={self.password},user status={self.user_status})"

class token_models(Base):
    __tablename__ = "token"
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    token = Column(Integer,ForeignKey("users.id"))