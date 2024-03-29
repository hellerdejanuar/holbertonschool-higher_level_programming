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
    STATE_IN = ' '.join(argv[4:])

    engine = create_engine(f'mysql+mysqldb://{USER_IN}:\
                       {PASSWD_IN}@{HOST_IN}/{DB_IN}')

    with Session(bind=engine) as session:
        query = session.query(State.name, State.id).\
            filter(State.name.like(STATE_IN))

        if query.all():
            for state in query:
                print(state.id)
        else:
            print('Not found')
