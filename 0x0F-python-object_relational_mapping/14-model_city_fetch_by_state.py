#!/usr/bin/python3

"""prints the State object with the name passed as arg from the database"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Ses = sessionmaker(bind=engine)
    ses = Ses()
    for _instance in (ses.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):

        print(_instance[0] + ": (" + str(_instance[1]) + ") " + _instance[2])
