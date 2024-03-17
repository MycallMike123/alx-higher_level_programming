#!/usr/bin/python3

"""A module that Contains State class and Base"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

custommetadata = MetaData()
Base = declarative_base(metadata=custommetadata)


class State(Base):
    """A Class with id and name attributes of each state"""

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
