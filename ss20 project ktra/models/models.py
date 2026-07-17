from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
class Classrooms(Base):
    __tablename__='classrooms'
    
    id=Column(Integer,primary_key=True,autoincrement=True)
    class_code=Column(String(10),nullable=False)
    class_name=Column(String(100),nullable=False)
    students=relationship('Students',back_populates='classrooms')
    
class Students(Base):
    __tablename__='students'
    
    id=Column(Integer,primary_key=True,autoincrement=True)
    student_code=Column(String(10),nullable=False)
    student_name=Column(String(100),nullable=False)
    email=Column(String(100),nullable=False)
    class_id=Column(Integer,ForeignKey('classrooms.id'),nullable=False)
    classrooms=relationship('Classrooms',back_populates='students')