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

@router.get("/categories/{category_id}/sessions/{session_id}", response_model=SessionSchema)
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
@router.post("/categories/{category_id}/sessions", response_model=SessionSchema)
def create_session(
    session: SessionCreateSchema,
    category_id: int, 
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
    ):
     
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can create categories")
    
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    new_session = SessionModel(**session.dict(), category_id=category_id)
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session



# =====================
# UPDATE (Admin only)
# =====================
@router.put("/categories/{category_id}/sessions/{session_id}", response_model=SessionSchema)
def update_session(
    session: SessionCreateSchema,
    category_id: int,
    session_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can update categories")

    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    
    if not category: 
        raise HTTPException(status_code=404, detail="Category not found")

    db_session = db.query(SessionModel).filter(
        SessionModel.id == session_id,
        SessionModel.category_id == category_id).first()
    
    if not db_session:
        raise HTTPException(status_code=404, detail="Session not found in this category")
    
    
    session_data = session.dict(exclude_unset=True)
    for key, value in session_data.items():
        setattr(db_session, key ,value)
    
    db.commit()
    db.refresh(db_session)
    return db_session

# =====================
# DELETE (Admin only)
# =====================
@router.delete("/categories/{category_id}/sessions/{session_id}")
def delete_session(
    category_id:int,
    session_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can update categories")

    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    
    if not category: 
        raise HTTPException(status_code=404, detail="Category not found")

    session = db.query(SessionModel).filter(
        SessionModel.id == session_id,
        SessionModel.category_id == category_id).first()
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found in this category")
    
    db.delete(session)
    db.commit()
    return {"message": f"Session with ID {session_id} has been deleted"}

    
    