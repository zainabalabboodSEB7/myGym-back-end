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

@router.get("categories/{category_id}/sessions/{session_id}")
def get_single_session(category_id:int, session_id: int, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()

    if not category: 
        raise HTTPException(status_code=404, detail="Category not found")

    session = db.query(SessionModel).filter(
        SessionModel.id == session_id,
        SessionModel.category_id == category_id).first()
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found in this category")
    
    return session


# =====================
# CREATE (Admin only)
# =====================


# =====================
# UPDATE (Admin only)
# =====================


# =====================
# DELETE (Admin only)
# =====================

