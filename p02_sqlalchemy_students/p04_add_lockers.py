from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from models_students import Base, Student, Locker

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Locker(number=1, student=4),
            Locker(number=2, student=1),
            Locker(number=3, student=5),
            Locker(number=4, student=2),
            Locker(number=5, student=3)
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(f"Error: {e}")
