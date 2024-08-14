"""Task 3
Write the function insert_instruments,
which will be responsible for completing the data in the instruments table.
The function should take two arguments:
 - a connection to the database
 - a list of records to be entered.
Test the function against the following list:
"""

from mysql.connector import connect, Error
from connection_details import *

instruments = [
    ('guitar', 'strings', 'medium'),
    ('piano', 'keyboard', 'hard'),
    ('harp', 'strings', 'hard'),
    ('triangle', 'percussion', 'easy'),
    ('flute', 'woodwind', 'medium'),
    ('violin', 'string', 'medium'),
    ('tambourine', 'percussion', 'easy'),
    ('organ', 'keyboard', 'hard')]


def insert_instruments(connection, instruments_list):
    with connection.cursor() as cursor:
        sql_statement = """
            INSERT INTO instruments 
            (name, family, difficulty)
            VALUES (%s, %s, %s);
        """
        cursor.executemany(sql_statement, instruments_list)
        connection.commit()


try:
    with connect(host=host, user=user, password=password, database='music') as conn:
        insert_instruments(conn, instruments)

except Error as e:
    print(e)
