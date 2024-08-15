from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(32))
    last_name = Column(String(32))

    def __repr__(self):
        return f"Student(first_name={self.first_name}, last_name={self.last_name})"

    def __str__(self):
        return f"Student #{self.id} {self.first_name} {self.last_name}"


class Locker(Base):
    __tablename__ = "lockers"
    number = Column(Integer, primary_key=True)
    student = Column(Integer, ForeignKey(Student.id))

    def __repr__(self):
        return f"Locker(number={self.number}, student={self.student})"

    def __str__(self):
        return f"Locker #{self.number} belongs to student: {self.student}"


class Address(Base):
    __tablename__ = "address"
    student = Column(Integer, ForeignKey(Student.id), primary_key=True)
    street_name = Column(String(50))
    number = Column(Integer)
    city = Column(String(50))

    def __repr__(self):
        return (f"Address(student={self.student}, "
                f"street_name={self.street_name}, "
                f"number={self.number},"
                f"city={self.city})")

    def __str__(self):
        return f"Address: {self.street_name} {self.number}, {self.city}"


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student = Column(Integer, ForeignKey(Student.id))
    grade = Column(Integer, nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"Grades(id={self.id}, student={self.student}, grade={self.grade}, date_created={self.date_created})"

    def __str__(self):
        return f"Student {self.student} has grade: {self.grade} ({self.date_created}) #{self.id}"
