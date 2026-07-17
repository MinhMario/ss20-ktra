from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from database import get_db
from service.service import * 
from schemas.schemas import * 
router=APIRouter(prefix="/students",
                 tags=['Students'])

@router.get("/", status_code=200)
def handle_show_all(request: Request, db: Session = Depends(get_db)):
    students = show_all(db)
    return JSONResponse(status_code=200, content={
        "statusCode": 200,
        "message": "Lấy danh sách sinh viên thành công!",
        "data": [s.model_dump() for s in students],
        "error": None,
        "path": str(request.url.path)
    })

@router.post("/", status_code=201)
def handle_create_students(data: CreateStudentRequest, request: Request, db: Session = Depends(get_db)):
    new_student = create_students(db, data)
    return JSONResponse(status_code=201, content={
        "statusCode": 201,
        "message": "Thêm mới sinh viên thành công!",
        "data": new_student.model_dump(),
        "error": None,
        "path": str(request.url.path)
    })
