from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host,
                 user=user,
                 password=password,
                 database="cinematic") as conn:
        print(conn)
        with conn.cursor() as cursor:
            """Task 3
            Write an SQL query that will create the following tables in the cinematic database:
                directors: director_id(PK), name, surname, rating
                movies: movie_id(PK), title, year, category, director_id(FK), rating
            """
            create_table_directors = """
                CREATE TABLE IF NOT EXISTS directors (
                    director_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                    name VARCHAR(30),
                    surname VARCHAR(30) NOT NULL,
                    rating INT
                ) DEFAULT CHARACTER SET utf8;
                """
            create_table_movies = """
                CREATE TABLE IF NOT EXISTS movies (
                    movie_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                    title VARCHAR(50),
                    year SMALLINT,
                    category VARCHAR(30),
                    director_id INT NOT NULL,
                    rating INT,
                    CONSTRAINT `movies_director` FOREIGN KEY (`director_id`) REFERENCES `directors` (director_id)
                ) DEFAULT CHARACTER SET utf8;
                """
            """Task 4 
            Execute the query you wrote earlier creating the tables in the cinematic database.
            """
            cursor.execute(create_table_directors)
            cursor.execute(create_table_movies)

except Error as e:
    print(e)
