from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey, inspect
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

engine = create_engine('sqlite:///students.db', echo=False)
Base = declarative_base()

student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', ForeignKey('STUDENTS.studentID'), primary_key=True),
    Column('course_id', ForeignKey('COURSES.courseID'), primary_key=True)
)

class Students(Base):
    __tablename__ = 'STUDENTS'

    studentID = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)

    courses = relationship("Courses", secondary=student_course, back_populates="students")

class Courses(Base):
    __tablename__ = 'COURSES'

    courseID = Column(Integer, primary_key=True)
    courseName = Column(String)
    courseDuration = Column(String)

    students = relationship("Students", secondary=student_course, back_populates="courses")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

students = [
    Students(name="Sheldon", surname="Cooper", age=25),
    Students(name="Leonard", surname="Hofstadter", age=25),
    Students(name="Howard", surname="Wolowitz", age=24),
    Students(name="Rajesh", surname="Koothrappali", age=24),
    Students(name="Ammy", surname="Farrah Fowler", age=23),
    Students(name="Penny", surname="Johnson", age=23),
    Students(name="Bernadette", surname="Rostenkowski", age=22),
    Students(name="Emily", surname="Sweeney", age=24),
    Students(name="Leslie", surname="Winkle", age=25),
    Students(name="Beverly", surname="Hofstadter", age=45),
    Students(name="Stuart", surname="Bloom", age=30),
    Students(name="Wil", surname="Wheaton", age=42),
    Students(name="Priya", surname="Koothrappali", age=27),
    Students(name="Barry", surname="Kripke", age=29),
    Students(name="Alex", surname="Jensen", age=26),
    Students(name="Ramona", surname="Nowitzki", age=28),
    Students(name="Janine", surname="Davis", age=41),
    Students(name="Kurt", surname="MacGregor", age=32),
    Students(name="Stephanie", surname="Barnett", age=26),
    Students(name="Claire", surname="Henderson", age=24)
]

courses = [
    Courses(courseName="Math", courseDuration="12 weeks"),
    Courses(courseName="Art", courseDuration="6 weeks"),
    Courses(courseName="History", courseDuration="20 weeks"),
    Courses(courseName="Physics", courseDuration="18 weeks"),
    Courses(courseName="Biology", courseDuration="14 weeks")
]

session.add_all(students + courses)
session.commit()

for student in students:
    student.courses = random.sample(courses, k=random.randint(1, 3))

session.commit()

def newStudent(name, surname, age, courseName):
    course = session.query(Courses).filter_by(courseName=courseName).first()
    if course != None:
        new_student = Students(name=name, surname=surname, age=age)
        new_student.courses.append(course)

        session.add(new_student)
        session.commit()

newStudent("Stefan", "Salvatore", 25, "History")
newStudent("Damon", "Salvatore", 27, "History")


for s in students:
    print(f"{s.name} visits {', '.join(c.courseName for c in s.courses)}")

def editStudentAge(name, age):
    student = session.query(Students).filter_by(name=name).first()
    if student is not None:
        student.age = age
        print(f"{name} new age is {age}")
    else:
        print(f"{name} not found")
    session.commit()

editStudentAge("Damon", 20)
editStudentAge("John", 20)

def deleteStudent(name):
    student = session.query(Students).filter_by(name=name).first()
    if student is not None:
        session.delete(student)
        print(f"{name} is deleted")
    else:
        print(f"{name} not found")
    session.commit()

deleteStudent("Damon")
deleteStudent("John")
