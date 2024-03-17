#!/usr/bin/python3

"""Creates the State "California" with City "San Francisco" from a DB"""

import sys
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Ses = sessionmaker(bind=engine)
    ses = Ses()

    addedState = State(name='California')
    addedCity = City(name='San Francisco')
    addedState.cities.append(addedCity)

    ses.add(addedState)
    ses.add(addedCity)
    ses.commit()
