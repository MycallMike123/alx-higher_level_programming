#!/usr/bin/python3

"""A module that Start link class to table in database"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Ses = sessionmaker(bind=engine)
    ses = Session()
    for instance in ses.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
