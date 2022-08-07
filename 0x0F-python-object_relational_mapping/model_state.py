#!/usr/bin/python3
""" states module """
""" contains the class definition of a State and an instance Base = declarative_base() """
""" WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine) """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String # ??
from sys import argv

#USER_IN = argv[1]
#PASSWD_IN = argv[2]
#DB_IN = argv[3]
#HOST_IN = 'localhost'

# engine = create_engine(f'mysql://{USER_IN}:{PASSWD_IN}@{HOST_IN}/{DB_IN}')
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
