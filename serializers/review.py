from pydantic import BaseModel, Field
from typing import Optional


class ReviewSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    content: str
    rating: int
    # session_id: int

    class Config:
        orm_mode = True