from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from models.session import SessionModel
from models.category import CategoryModel
from models.user import UserModel
from serializers.session import SessionSchema, SessionCreateSchema
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

# =====================
# READ ENDPOINTS (All users)
# =====================
@router.get("/categories/{category_id}/sessions", response_model=List[SessionSchema])
def get_sessions(category_id: int, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category.sessions


# =====================
# CREATE (Admin only)
# =====================


# =====================
# UPDATE (Admin only)
# =====================


# =====================
# DELETE (Admin only)
# =====================

