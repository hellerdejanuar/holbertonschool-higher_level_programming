#!/usr/bin/python3
""" Fetches the first state ordered by ID """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy import select
from sys import argv

if __name__ == "__main__":

    USER_IN = argv[1]
    PASSWD_IN = argv[2]
    DB_IN = argv[3]
    HOST_IN = 'localhost'

    engine = create_engine(f'mysql+mysqldb://{USER_IN}:\
                       {PASSWD_IN}@{HOST_IN}/{DB_IN}')
    session = Session(bind=engine)

    query = session.query(State.name, State.id).filter(State.name.op('regexp')('.*a.*'))
    if query:
        for state in query:
            print(f'{state.id}: {state.name}')
    else:
        print()

    session.close()
