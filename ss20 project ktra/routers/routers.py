from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from database import get_db
from service.service import * 
from schemas.schemas import * 
router=APIRouter(prefix="/students",
                 tags=['Students'])

@router.get("/",status_code=200,response_model=List[StudentResponse])
def handle_show_all(db:Session=Depends(get_db)):
    all=show_all(db)
    return all
@router.post("/",status_code=201,response_model=StudentResponse)
def handle_create_students(data:CreateStudentRequest,db:Session=Depends(get_db)):
    new_student=create_students(db,data)
    return new_student