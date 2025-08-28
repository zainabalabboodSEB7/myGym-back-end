from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship
from database import BaseModel

class Instructor(BaseModel):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    

    # Relationships : OneToMany
    classes = relationship('ClassModel', back_populates='instructors')
