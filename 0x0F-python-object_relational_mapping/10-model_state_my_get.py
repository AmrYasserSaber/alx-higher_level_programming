#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}')

    Session = sessionmaker(bind=engine)
    session = Session()

    state_id = session.query(State.id).filter(State.name == argv[4]).first()
    if (state_id):
        print(state_id.id)
    else:
        print("Not found")