from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class CategoryModel(BaseModel):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    instructor_id = Column(Integer, ForeignKey("instructors.id"), nullable=True)

    instructor = relationship("InstructorModel", back_populates="categories")
    sessions = relationship("SessionModel", back_populates="category", cascade="all, delete")


