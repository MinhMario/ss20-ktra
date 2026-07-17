from pydantic import BaseModel,ConfigDict
from typing import List
class CreateStudentRequest(BaseModel):
    student_code:str
    full_name:str
    email:str
    class_id:int
class ClassroomResponse(BaseModel):
    id:int
    class_code:str
    class_name:str
class StudentResponse(BaseModel):
    student_code:str
    full_name:str
    email:str
    classroom:ClassroomResponse
    model_config=ConfigDict(from_attributes=True)

    