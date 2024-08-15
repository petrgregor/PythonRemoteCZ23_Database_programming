from connect_db import session
from models_students import Student, Locker


print("Join Student and Lockers.")
rows = session.query(Student).join(Locker)
for row in rows:
    print(row)

print('-'*80)
print("Student with locker #4")
rows = session.query(Student).join(Locker).filter(Locker.number == 4)
for row in rows:
    print(row)

print('-'*80)
print("Join Student and Lockers.")
rows = session.query(Student, Locker).join(Locker).order_by(Locker.number)
print(rows)
for row in rows:
    print(row)
    print(f"Locker #{row[1].number} belongs to {row[0]}")
print('-'*40)
for student, locker in rows:
    print(f"{locker}: {student}")
print('-'*40)
for row in rows:
    student, locker = row
    print(f"{locker}: {student}")
