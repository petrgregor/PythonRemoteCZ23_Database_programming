from sqlalchemy import and_, or_, desc

from connect_db import session
from models_students import Student

print("All students in database:")
# SELECT * FROM students;
students = session.query(Student).all()
print(f"students: {students}")
for student in students:
    print(student)

print("-"*80)
print("Number of students in database:")
s = session
total = s.query(Student).count()
print(f"Total: {total}")

print("-"*80)
print("All students with id >= 3")
"""
SELECT * FROM students 
WHERE students.id >= 3
"""
rows = s.query(Student).filter(Student.id >= 3)
print(rows)
for row in rows:
    print(row)

print("-"*80)
print("All student with surname starting as 'Svob'")
rows = s.query(Student).filter(Student.last_name.like("Svob%"))
for row in rows:
    print(row)

print("-"*80)
print("All students with id >= 5 and surname starting as 'Čer'")
rows = s.query(Student).filter(Student.id >= 5, Student.last_name.like("Čer%"))
#rows = s.query(Student).filter(and_(Student.id >= 5, Student.last_name.like("Čer%")))
for row in rows:
    print(row)

print("-"*80)
print("All students with name or surname starting as 'B'")
rows = s.query(Student).filter(or_(Student.first_name.like("B%"), Student.last_name.like("B%")))
print(rows)
#s.add(Student(first_name="Gusta", last_name="Beneš"))
#s.commit()
for row in rows:
    print(row)
print('-'*40)
#s.add(Student(first_name="Helena", last_name="Budínská"))
#s.commit()
for row in rows:
    print(row)

print('-'*80)
# TODO: Distinct
rows = s.query(Student).distinct(Student.first_name).all()
# DISTINCT ON is currently supported only by the PostgreSQL dialect
for row in rows:
    print(row)

print('-'*80)
print("All students order by last_name and first_name")
rows = s.query(Student).order_by(Student.last_name, Student.first_name)
for row in rows:
    print(row)

print('-'*80)
print("All students order by last_name and first_name descending")
rows = s.query(Student).order_by(desc(Student.last_name), desc(Student.first_name))
for row in rows:
    print(row)

print('-'*80)
print("Student with id >= 3 order by last_name")
rows = s.query(Student).filter(Student.id >= 3).order_by(Student.last_name)
for row in rows:
    print(row)

print('-'*80)
print("Offset = 3 (skip first 3 records)")
rows = s.query(Student).offset(3)
for row in rows:
    print(row)

print('-'*80)
print("Students with id > 5, skip first 2 lines")
rows = s.query(Student).filter(Student.id > 5).offset(2)
print(rows)
for row in rows:
    print(row)

print('-'*80)
print("Students --- limit = 3 (select first 3 records)")
rows = s.query(Student).order_by(Student.last_name).limit(3)
for row in rows:
    print(row)

print('-'*80)
print("First student")
rows = s.query(Student).limit(1)  # list of one student
for row in rows:
    print(row)
print('-'*40)
result = s.query(Student).first()  # one student (one object)
#for r in result:
#    print(r)
# TypeError: 'Student' object is not iterable
print(result)

print('-'*80)
print("Student with id = 3")
rows = s.query(Student).filter(Student.id == 3)  # list of one student
for row in rows:
    print(row)

# LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
result = s.query(Student).get(3)  # one student (one object)
print(result)
