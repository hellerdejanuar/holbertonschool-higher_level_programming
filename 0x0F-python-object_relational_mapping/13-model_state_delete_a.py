#!/usr/bin/python3
""" changes the name of a State object from the database """

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

    with Session(bind=engine) as session:
        delete_query = session.query(State).filter(State.name.contains("a"))
        for obj in delete_query:
            session.delete(obj)
        session.commit()
