"""Task 2
Write a script that will create a music database with the table:
instruments: instrument_id(PK, autoincrement), name, family, difficulty(enum - easy, medium, hard)
"""

from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password) as conn:
        print(conn)
        with conn.cursor() as cursor:
            create_database = "CREATE DATABASE IF NOT EXISTS music"
            cursor.execute(create_database)
            print("Databáze 'music' byla vytvořena.")
            create_table_instruments = """
                CREATE TABLE IF NOT EXISTS music.instruments(
                    instrument_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                    name VARCHAR(30) NOT NULL,
                    family VARCHAR(30) NOT NULL,
                    difficulty ENUM('easy', 'medium', 'hard') NOT NULL
                )
            """
            cursor.execute(create_table_instruments)
            print("Tabulka 'instruments' byla vytvořena.")

except Error as e:
    print(e)
