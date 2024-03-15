#!/usr/bin/python3

"""prints the State object with the name passed as arg from the database"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Ses = sessionmaker(bind=engine)
    session = Ses()
    n_state = State(name='Louisiana')
    session.add(n_state)
    _instance = session.query(State).filter_by(name='Louisiana').first()
    print(_instance.id)
    session.commit()
