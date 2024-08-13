from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password, database="cinematic") as conn:
        print(conn)
        with conn.cursor() as cursor:
            """Task 7
            Write an SQL query that will remove the tables from the cinematic database. Make an inquiry.
            """
            sql_statement = """DROP TABLE movies;"""
            cursor.execute(sql_statement)
            sql_statement = """DROP TABLE directors;"""
            cursor.execute(sql_statement)

except Error as e:
    print(e)
