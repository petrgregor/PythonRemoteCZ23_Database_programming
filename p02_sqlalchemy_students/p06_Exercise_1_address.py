"""Exercise 1
- Create a new table called address
- It should include the following fields:
  - student int, foreign key, primary key
  - street_name string
  - number int
  - city string
- Add an Address for each student
- Print out all students along with their addresses using a join()
"""
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from models_students import *

Base.metadata.create_all(db)

try:
    # Add an Address for each student
    session.add_all(
        [
            Address(student=1, street_name="Hlavní", number=5, city="Brno"),
            Address(student=2, street_name="Jarní", number=7, city="Praha"),
            Address(student=3, street_name="Letní", number=13, city="Ostrava"),
            Address(student=4, street_name="Podzimní", number=1, city="Olomouc"),
            Address(student=5, street_name="Zimní", number=54, city="Jihlava"),
            Address(student=6, street_name="Náměstí Svobody", number=3, city="Znojmo"),
            Address(student=7, street_name="Malinovského náměstí", number=2, city="Brno"),
            Address(student=8, street_name="Nádražní", number=501, city="Praha"),
            Address(student=9, street_name="Ostravská", number=14, city="Brno"),
        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(f"Error: {e}")


# Print out all students along with their addresses using a join()
print("All students with their address:")
rows = session.query(Student, Address).join(Address)
for student, address in rows:
    print(f"{student}: {address}")

print('-'*80)
print("All students with their address2:")
rows = session.query(Address, Student).join(Address)
for address, student in rows:
    print(f"{student}: {address}")

print('-'*80)
print("All students from Brno:")
#rows = session.query(Student, Address).join(Address).filter(Address.city == "Brno")
rows_Brno = rows.filter(Address.city == "Brno")
for student, address in rows_Brno:
    print(f"{student}: {address}")

print('-'*80)
rows_Brno_sorted = rows_Brno.order_by(Student.last_name)
for student, address in rows_Brno_sorted:
    print(f"{student}: {address}")

print('-'*80)
print("Student Adam Bernau moved to street 'Vedlejší'")
students = session.query(Student, Address).join(Address).filter(and_(Student.first_name == "Adam", Student.last_name == "Bernau"))
for student, address in students:
    print(f"{student} {address}")
student, address = students[0]
print(student, address)
address.street_name = "Vedlejší"
session.commit()
student, address = students[0]
print(student, address)
