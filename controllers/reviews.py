from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from models.session import SessionModel
from models.category import CategoryModel
from models.review import ReviewModel
from serializers.review import ReviewSchema
from database import get_db

router = APIRouter()


# =====================
# READ ENDPOINT (All users)
# =====================
@router.get("/categories/{category_id}/sessions/{session_id}/reviews", response_model=List[ReviewSchema])
def get_session_reviews(category_id: int, session_id: int, db: Session = Depends(get_db)):
    # check if category exists
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    # check if session exists inside this category
    session = (
        db.query(SessionModel)
        .filter(SessionModel.id == session_id, SessionModel.category_id == category_id)
        .first()
    )
    if not session:
        raise HTTPException(status_code=404, detail="Session not found in this category")

    # return reviews for that session
    return session.reviews

@router.get("/categories/{category_id}/sessions/{session_id}/reviews/{review_id}", response_model=ReviewSchema)
def get_session_reviews(category_id: int, session_id: int, review_id:int, db: Session = Depends(get_db)):
    # check if category exists
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    # check if session exists inside this category
    session = (
        db.query(SessionModel)
        .filter(SessionModel.id == session_id, SessionModel.category_id == category_id)
        .first()
    )
    if not session:
        raise HTTPException(status_code=404, detail="Session not found in this category")
    
    review = db.query(ReviewModel).filter(
        ReviewModel.id == review_id,
        ReviewModel.session_id == session_id
    ).first()

    if not review:
        raise HTTPException(status_code=404, detail="Review not found in this session")

    # return reviews for that session
    return review



