from pydantic import BaseModel, Field
from typing import Optional
from serializers.user import UserResponseSchema

class ReviewSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    content: str
    rating: int
    user_id: int
    session_id: int
    user: UserResponseSchema

    class Config:
        orm_mode = True

class ReviewCreateSchema(BaseModel):
    content: str
    rating: int
    
    class Config:
        orm_mode = True