@app.get("/")
def home():
    return {"message": "CI/CD pipeline verified 🚀🔥"}
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:password@postgres:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    marks = Column(Float)
    attendance = Column(Float)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD pipeline verified 🚀🔥"}

@app.post("/students")
def add_student(name: str, marks: float, attendance: float):
    db = SessionLocal()
    student = Student(name=name, marks=marks, attendance=attendance)
    db.add(student)
    db.commit()
    db.refresh(student)
    db.close()
    return student

@app.get("/students")
def get_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return students
