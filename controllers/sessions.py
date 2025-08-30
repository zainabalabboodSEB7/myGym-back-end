from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from models.session import SessionModel   
from models.user import User              
from serializers.session import SessionResponse, SessionCreate, SessionUpdate
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()


# =====================
# READ ENDPOINTS (All users)
# =====================
@router.get("/sessions", response_model=List[SessionResponse])
def get_sessions(db: Session = Depends(get_db)):
    sessions = db.query(SessionModel).all()
    return sessions


@router.get("/sessions/{session_id}", response_model=SessionResponse)
def get_single_session(session_id: int, db: Session = Depends(get_db)):
    session_obj = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session_obj:
        raise HTTPException(status_code=404, detail="Session not found")
    return session_obj


# =====================
# CREATE (Admin only)
# =====================
@router.post("/sessions", response_model=SessionResponse)
def create_session(
    new_session: SessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admin can create sessions")

    session_obj = SessionModel(**new_session.dict())
    db.add(session_obj)
    db.commit()
    db.refresh(session_obj)
    return session_obj


# =====================
# UPDATE (Admin only)
# =====================
@router.put("/sessions/{session_id}", response_model=SessionResponse)
def update_session(
    session_id: int,
    session_data: SessionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admin can update sessions")

    db_session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not db_session:
        raise HTTPException(status_code=404, detail="Session not found")

    update_data = session_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_session, key, value)

    db.commit()
    db.refresh(db_session)
    return db_session


# =====================
# DELETE (Admin only)
# =====================
@router.delete("/sessions/{session_id}")
def delete_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admin can delete sessions")

    db_session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not db_session:
        raise HTTPException(status_code=404, detail="Session not found")

    db.delete(db_session)
    db.commit()
    return {"message": f"Session with ID {session_id} has been deleted"}
