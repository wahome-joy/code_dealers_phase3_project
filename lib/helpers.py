from sqlalchemy import  String, Integer, Column, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User (Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
