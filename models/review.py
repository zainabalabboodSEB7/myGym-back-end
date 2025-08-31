from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class ReviewModel(BaseModel):

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)  

    session_id = Column(Integer, ForeignKey('sessions.id'), nullable=False)

    session = relationship("SessionModel", back_populates="reviews")
