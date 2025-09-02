from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from models.instructor import InstructorModel
from serializers.instructor import InstructorSchema
from database import get_db

router = APIRouter()

# -----------------------
# GET all instructors
# -----------------------
@router.get("/instructors", response_model=List[InstructorSchema])
def get_instructors(db: Session = Depends(get_db)):
    instructors = db.query(InstructorModel).all()
    return instructors
