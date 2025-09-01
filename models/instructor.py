from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship
from .base import BaseModel
from .user import UserModel

class InstructorModel(BaseModel):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))


    # Relationships : 
    user = relationship('UserModel', back_populates='instructors')
    categories = relationship("CategoryModel", back_populates="instructor")
