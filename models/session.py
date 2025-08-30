from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class SessionModel(BaseModel):

    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)

    # Specific columns 
    name = Column(String)
    description = Column(String)
    duration_minutes = Column(Integer)
    capacity = Column(Integer)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # Relationships
    # users = relationship("UserModel", back_populates="sessions")
    # instructor = relationship("InstructorModel", back_populates="sessions")
    category = relationship("CategoryModel", back_populates="sessions")
    # reviews = relationship("ReviewModel", back_populates= "sessions")


