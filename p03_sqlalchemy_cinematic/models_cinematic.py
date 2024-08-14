from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Directors(Base):
    __tablename__ = "directors"
    director_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(30))
    surname = Column(String(30), nullable=False)
    rating = Column(Integer)


class Movies(Base):
    __tablename__ = "movies"
    movie_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(50))
    year = Column(Integer)
    category = Column(String(30))
    director_id = Column(Integer, ForeignKey(Directors.director_id), nullable=False)  # Task 2: Add relationships for the table (director_id - FK):
    rating = Column(Integer)
