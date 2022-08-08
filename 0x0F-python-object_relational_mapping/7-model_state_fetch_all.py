#!/usr/bin/python3
""" Table fetcher """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sys import argv

if __name__ == '__main__':
    USER_IN = argv[1]
    PASSWD_IN = argv[2]
    DB_IN = argv[3]
    HOST_IN = 'localhost'

    engine = create_engine(f'mysql+mysqldb://{USER_IN}:\
                             {PASSWD_IN}@{HOST_IN}/{DB_IN}')
    with Session(bind=engine) as session:

        query = session.query(State.name, State.id).all()
        for name, state_id in query:
            print(f'{state_id}: {name}')

        session.close()
