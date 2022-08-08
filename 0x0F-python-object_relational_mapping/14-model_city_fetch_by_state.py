#!/usr/bin/python3
""" Table fetcher """
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sys import argv

USER_IN = argv[1]
PASSWD_IN = argv[2]
DB_IN = argv[3]
HOST_IN = 'localhost'

engine = create_engine(f'mysql+mysqldb://{USER_IN}:{PASSWD_IN}@{HOST_IN}/{DB_IN}')

with Session(bind=engine) as session:
    city_q = (session.query(City)
            .join(State, State.id == City.state_id)
            .all())

    for obj in city_q:
        print(obj.__dict__)

