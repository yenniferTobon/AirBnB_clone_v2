#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="State", cascade="all, delete-orphan")

    @property
    def cities(self):
        if state_id == State.id:
            return self._cities;

