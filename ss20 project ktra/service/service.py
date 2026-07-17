from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.models import Students,Classrooms
from schemas.schemas import *

def show_all(db:Session):
    all=db.query(Students).all()
    return all
def create_students(db:Session,data:CreateStudentRequest):
    class_id=db.query(Classrooms).filter(Classrooms.id==data.class_id).first()
    if not class_id :
        raise HTTPException(status_code=404)
    student_code=db.query(Students).filter(Students.student_code==data.student_code).first()
    if student_code:
        raise HTTPException(status_code=400)
    new_student=Students(
        student_code=data.student_code,
        student_name=data.full_name,
        email=data.email,
        class_id=data.class_id  
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
