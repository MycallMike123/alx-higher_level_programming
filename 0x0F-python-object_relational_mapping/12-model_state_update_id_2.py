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
    ses = Ses()
    _instance = ses.query(State).filter_by(id=2).first()
    _instance.name = 'New Mexico'
    ses.commit()
