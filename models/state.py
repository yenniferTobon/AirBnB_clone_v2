#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all,delete")

    @property
    def city(self):
        """returns the list of City instances with state_id"""
        all_cities = storage.all(City)
        cities_list = {}
        for city in all_cities:
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
