from pydantic import BaseModel, Field
from typing import Optional, List
from .user import UserResponseSchema
from .review import ReviewSchema
from datetime import datetime

class SessionSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str
    description: str
    duration_minutes: int
    capacity: int
    start_time: datetime
    end_time: datetime
    # Relationships
    users: List[UserResponseSchema] = []
    # instructor: InstructorResponseSchema
    # category: "CategorySchema"
    reviews: List[ReviewSchema] = []

    class Config:
        orm_mode = True

class SessionCreateSchema(BaseModel):
    name: str
    description: str
    duration_minutes: int
    capacity: int
    start_time: datetime
    end_time: datetime
    # instructor_id: int
    # category_id: int

