import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    nick = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False )
    email = Column(String(250), nullable=False, unique=True)
    

class Favourite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    favourite_user = Column(Integer, ForeignKey('user.id'))
    favourite_char = Column(Integer, ForeignKey('characters.id'))
    favourite_planets = Column(Integer, ForeignKey('planets.id'))
    favourite_vehicles = Column(Integer, ForeignKey('vehicles.id'))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    height= Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    description = Column(String(250))
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    hyperdrive_rating = Column(String(250))
    MGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    pilots = Column(String(250))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')