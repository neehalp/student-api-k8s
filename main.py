from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create FastAPI app
app = FastAPI()

# Database connection
DATABASE_URL = "postgresql://postgres:password@postgres:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# Student table model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    marks = Column(Float)
    attendance = Column(Float)


# Create tables in database
Base.metadata.create_all(bind=engine)


# Home route
@app.get("/")
def home():
    return {"message": "CI/CD pipeline verified 🚀🔥"}


# Add student
@app.post("/students")
def add_student(name: str, marks: float, attendance: float):
    db = SessionLocal()
    student = Student(name=name, marks=marks, attendance=attendance)
    db.add(student)
    db.commit()
    db.refresh(student)
    db.close()
    return student


# Get all students
@app.get("/students")
def get_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return students
