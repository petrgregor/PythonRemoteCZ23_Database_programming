"""Task 1
From python, connect to the mysql server. Then create the cinematic database.
"""

from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password) as conn:
        print(conn)
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE cinematic;")
        print("Database 'cinematic' created.")

except Error as e:
    print(e)

"""Task 2
Connect to the mysql server by setting the cinematic base as the home / default base.
"""
try:
    with connect(host=host,
                 user=user,
                 password=password,
                 database="cinematic") as conn:
        print(conn)

except Error as e:
    print(e)
