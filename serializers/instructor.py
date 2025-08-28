from pydantic import BaseModel, Field
from typing import Optional, List

from serializers.user import UserResponseSchema
from serializers.class_model import ClassSchema  

class InstructorSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str

    # Relationships
    classes: List[ClassSchema] = []  
    user: Optional[UserResponseSchema] = None  

    class Config:
        orm_mode = True  

class InstructorCreateSchema(BaseModel):
    name: str
