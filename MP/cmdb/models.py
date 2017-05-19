from django.db import models

# Create your models here.

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# from MP.MP.settings import DATABASES

engine = create_engine("mysql+pymysql://root:python@192.168.1.234:33306/MP?charset=utf8")
Base = declarative_base()

class user(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    owner = Column(String(16))
    user = Column(String(16))
    password = Column(String(16))
    remarks = Column(String(64))

class host(Base):
    __tablename__ = "host"
    id = Column(Integer,primary_key=True)
    administarator = Column(String(16),nullable=True)
    host = Column(String(16))
    ip = Column(String(16))
    port = Column(String(4))
    server = Column(String(256))
    business = Column(String(256))
# Base.metadata.create_all(engine)


