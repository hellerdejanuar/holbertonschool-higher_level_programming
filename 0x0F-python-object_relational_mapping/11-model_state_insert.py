#!/usr/bin/python3
""" Adds the State object “Louisiana” to the database """

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
    NEW_STATE_NAME = 'Louisiana'

    engine = create_engine(f'mysql+mysqldb://{USER_IN}:\
                       {PASSWD_IN}@{HOST_IN}/{DB_IN}')

    # New state init --
    new_state = State(name=NEW_STATE_NAME)

    # Add to the database
    with Session(bind=engine) as session:

        session.add(new_state)
        session.commit()
        print(new_state.id)
