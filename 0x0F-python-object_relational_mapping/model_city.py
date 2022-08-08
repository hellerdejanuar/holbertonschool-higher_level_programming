#!/usr/bin/python3
""" contains the class definition of a city """
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.schema import ForeignKey

class City(Base):
    """ states class """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
               autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
