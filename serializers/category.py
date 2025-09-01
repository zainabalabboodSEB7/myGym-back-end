from pydantic import BaseModel, Field
from typing import Optional, List
from .session import SessionSchema
from .instructor import InstructorSchema


class CategorySchema(BaseModel):
    id: Optional[int] = Field(default=None) # This makes sure you don't have to explicitly add an id when sending json data
    name: str
    description: str
    instructor_id: Optional[int] = None
    instructor: Optional[InstructorSchema] = None  

    sessions: List[SessionSchema] = []

class CategoryCreateSchema(BaseModel):
    name: str
    description: str
    instructor_id: Optional[int] = None

    class Config:
        orm_mode = True
