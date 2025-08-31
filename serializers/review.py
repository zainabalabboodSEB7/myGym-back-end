from pydantic import BaseModel, Field
from typing import Optional


class ReviewSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    content: str
    rating: int
    user_id: int
    session_id: int

    class Config:
        orm_mode = True

class ReviewCreateSchema(BaseModel):
    content: str
    rating: int
    
    class Config:
        orm_mode = True