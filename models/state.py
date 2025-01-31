#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_t
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_t == 'db':
        name = Column(String(128), nullable=False)
        cities = relationshop('City', backref='state',
                cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """Return list of city instance with state_id
                showing relationship between city and state
            """
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
