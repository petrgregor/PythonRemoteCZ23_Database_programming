from datetime import datetime

from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from models_students import *

print("All grades:")
rows = session.query(Student, Grade).join(Grade)
for student, grade in rows:
    print(f"{student}: {grade}")

print('-'*80)
print("Print out all grades per each student using filter")
students = session.query(Student).all()
for student in students:
    print(f"{student}:")
    grades = session.query(Grade).filter(Grade.student == student.id)
    if grades.count() == 0:
        print(f"\tNo grades")
    for grade in grades:
        print(f"\t{grade}")

print("-"*80)
print("Delete")
grades = session.query(Grade).all()
for grade in grades:
    print(grade)
session.query(Grade).filter(Grade.id == 2).delete()
session.commit()
print('-'*80)
grades = session.query(Grade).all()
for grade in grades:
    print(grade)

print("="*80)
print("Výpis studenta s id == 2:")
print("Výpis studentů s id různých od 2:")
print("Výpis studentů, jejichž jméno začíná na 'A':")
print("Výpis studentů, jejichž jméno začíná na 'A' bez ohledu na velikost písmen:")
print("Výpis studentů, jejichž jméno nezačíná na 'A':")
print("Výpis studentů, jejichž jméno nezačíná na 'A' bez ohledu na velikost písmen:")
print("Výpis studentů z Brna, Olomouce a Znojma:")  # Address.city.in_(["Brno", "Olomouc", "Znojmo"])
print("Výpis studentů, kteří nejsou z Brna, Olomouce a Znojma:")  # not_in
print("Výpis všech studentů, jejichž příjmení začíná na 'N' a jsou z Ostravy")
print("Výpis všech studentů, jejichž příjmení začíná na 'N', nebo jsou z Olomouce")
print("Výpis všech studentů a adres, uspořádat podle příjmení studenta")
print("Výpis všech studentů a adres, uspořádat podle města")
print("Výpis všech známek všech studentů:")
print("Výpis počtu známek všech studentů:")
print("Výpis průměrné známky všech studentů:")
print("Výpis všech studentů, kteří nemají žádné hodnocení:")
print("Výpis studenta s nejlepším průměrným hodnocením:")
