"""Task 1
Connect to the mysql server, setting the cinematic base as the home / default base. Create a table definition using SQLAlchemy:
    Directors (class) - table directors: director_id (PK), name, surname, rating
    Movies (class) - table movies: movie_id (PK), title, year, category, director_id, rating
"""

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from p01_mysql.connection_details import *
from models_cinematic import *


CONNECTION_STRING = "mysql+mysqlconnector://{user}:{password}@{host}/{database}"
db = create_engine(
    CONNECTION_STRING.format(
        user=user, password=password, host=host, database="cinematic2"
    )
)

print(f"db.url = {db.url}")
if not database_exists(db.url):
    create_database(db.url)

Base.metadata.create_all(db)  # vytvoří všechny tabulky z models_cinematic.py
