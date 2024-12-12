from config.database import Base, engine
from sqlalchemy import Column, Integer, String, Float


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    year = Column(Integer)
    overview = Column(String)
    rating = Column(Float)
    category = Column(String)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Float)

Base.metadata.create_all(engine)
