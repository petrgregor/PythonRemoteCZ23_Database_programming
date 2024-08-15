"""Exercise 2
- Create a table called grades
- It should include the following fields:
  - id int, primary key, autoincrement
  - student int, foreign key
  - grade int or string - whichever you prefer
  - date_created datetime
- Add some grades for each student
- Print out all grades per each student using filter
"""
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from models_students import *

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Grade(student=1, grade=1, date_created=datetime(2024, 5, 1, 12, 30)),
            Grade(student=1, grade=2, date_created=datetime(2024, 5, 2, 13, 35)),
            Grade(student=1, grade=2, date_created=datetime(2024, 5, 3, 8, 25)),
            Grade(student=1, grade=1, date_created=datetime(2024, 5, 4, 7, 20)),
            Grade(student=2, grade=3, date_created=datetime(2024, 5, 15, 12, 15)),
            Grade(student=2, grade=1, date_created=datetime(2024, 6, 1, 6, 19)),
            Grade(student=2, grade=4, date_created=datetime(2024, 5, 1, 12, 55)),
            Grade(student=3, grade=3, date_created=datetime(2024, 5, 1, 7, 39)),
            Grade(student=4, grade=2, date_created=datetime(2024, 7, 15, 12, 30)),
            Grade(student=5, grade=1, date_created=datetime(2024, 7, 1, 12, 30)),
            Grade(student=5, grade=4, date_created=datetime(2024, 7, 24, 8, 30)),
            Grade(student=5, grade=2, date_created=datetime(2024, 6, 25, 9, 30)),
            Grade(student=5, grade=2, date_created=datetime(2024, 4, 4, 10, 22)),
            Grade(student=6, grade=2, date_created=datetime(2024, 4, 1, 11, 33)),
            Grade(student=9, grade=3, date_created=datetime(2024, 2, 2, 14, 44)),
            Grade(student=9, grade=1, date_created=datetime(2024, 3, 3, 9, 55)),
            Grade(student=9, grade=1, date_created=datetime(2024, 5, 1, 9, 11)),
            Grade(student=1, grade=1, date_created=datetime(2024, 8, 5, 12, 00)),
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(f"Error: {e}")
