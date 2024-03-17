#!/usr/bin/python3

"""Module that prints the State obj with the name passed as arg from the DB"""

import sys
from sqlalchemy.orm import relationship
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Ses = sessionmaker(bind=engine)
    ses = Ses()

    for _instance in ses.query(State).order_by(State.id):
        for city_ins in _instance.cities:
            print(city_ins.id, city_ins.name, sep=": ", end="")
            print(" -> " + _instance.name)
