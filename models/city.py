#!/usr/bin/python3
"""Module contains City class."""

from models.base_model import BaseModel


class City(BaseModel, Base):
    """Class representing a City.
    Attributes:
    __tablename (str): input
    name (str): input
    state)id(str): input
    places(str): input
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
