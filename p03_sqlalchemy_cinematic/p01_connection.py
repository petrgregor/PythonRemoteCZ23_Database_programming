#  pip install sqlalchemy
from sqlalchemy import create_engine
from p01_mysql.connection_details import *

                  # dialect+connector://user:pass@host:port/database
#db = create_engine('mysql+mysqlconnector://test:test@localhost:3306/cinematic')

CONNECTION_STRING = "mysql+mysqlconnector://{user}:{password}@{host}/{database}"
db = create_engine(
    CONNECTION_STRING.format(
        user=user, password=password, host=host, database="cinematic"
    )
)
