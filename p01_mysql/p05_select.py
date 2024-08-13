from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host,
                 user=user,
                 password=password,
                 database="cinematic") as conn:
        print(conn)
        with conn.cursor() as cursor:
            sql_statement = """SELECT * FROM movies;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            print("========= MOVIES =========")
            for movie in movies:
                print(movie)

            sql_statement = """SELECT * FROM directors;"""
            cursor.execute(sql_statement)
            directors = cursor.fetchall()
            print("========= DIRECTORS =========")
            for director in directors:
                print(director)

            """Task 6
            Write an SQL query that will return all movies from 2002. Make an inquiry.
            """

            sql_statement = """SELECT * FROM movies WHERE year = 2002;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            print("========= MOVIES (year = 2002) =========")
            for movie in movies:
                print(movie)

            sql_statement = """SELECT * FROM movies WHERE year = 1994;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            print("========= MOVIES (year = 1994) =========")
            for movie in movies:
                print(movie)

except Error as e:
    print(e)
