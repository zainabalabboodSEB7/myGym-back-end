from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt

from config.environment import jwt_secret

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserModel(BaseModel):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)  # Each username must be unique
    email = Column(String, unique=True)  # Each email must be unique
    password_hash = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)
    reviews = relationship("ReviewModel", back_populates="user", cascade="all, delete")

    teas = relationship('TeaModel', back_populates='user')

    # Auth Methods

    def set_password(self, password: str):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)

    def generate_token(self):
        # Define the payload
        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),  # Expiration time (1 day)
            "iat": datetime.now(timezone.utc),  # Issued at time
            "sub": str(self.id),  # Subject - the user ID
            "username": self.username,
            "is_admin": self.is_admin
        }

        # Create the JWT token
        token = jwt.encode(payload, jwt_secret, algorithm="HS256")

        return token