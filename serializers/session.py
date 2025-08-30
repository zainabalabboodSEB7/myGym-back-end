from pydantic import BaseModel, Field
from typing import Optional, List
from .user import UserResponseSchema

class SessionSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str
    description: str
    duration_minutes: int
    capacity: int

    # Relationships
    users: List[UserResponseSchema] = []
    # instructor: InstructorResponseSchema
    # category: "CategorySchema"
    # reviews: List[ReviewResopnseSchema]

    class Config:
        orm_mode = True

class SessionCreateSchema(BaseModel):
    name: str
    description: str
    duration_minutes: int
    capacity: int
    # instructor_id: int
    # category_id: int

