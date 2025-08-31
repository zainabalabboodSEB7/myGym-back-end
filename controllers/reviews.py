from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from models.session import SessionModel
from models.category import CategoryModel
from models.user import UserModel
from models.review import ReviewModel
from serializers.review import ReviewSchema, ReviewCreateSchema
from database import get_db

from dependencies.get_current_user import get_current_user


router = APIRouter()


# =====================
# READ ENDPOINT (All users)
# =====================
@router.get("/categories/{category_id}/sessions/{session_id}/reviews", response_model=List[ReviewSchema])
def get_session_reviews(category_id: int, session_id: int, db: Session = Depends(get_db)):
   
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    session = (
        db.query(SessionModel)
        .filter(SessionModel.id == session_id, SessionModel.category_id == category_id)
        .first()
    )
    if not session:
        raise HTTPException(status_code=404, detail="Session not found in this category")

    return session.reviews

@router.get("/categories/{category_id}/sessions/{session_id}/reviews/{review_id}", response_model=ReviewSchema)
def get_session_reviews(
    category_id: int, 
    session_id: int, 
    review_id:int, 
    db: Session = Depends(get_db)
    ):
    
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    
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

    return review

# =====================
# CREATE 
# =====================
@router.post(
    "/categories/{category_id}/sessions/{session_id}/reviews",
    response_model=ReviewSchema,
)
def create_review(
    review: ReviewCreateSchema,
    category_id: int,
    session_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user) 
):
    
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    session = (
        db.query(SessionModel)
        .filter(SessionModel.id == session_id, SessionModel.category_id == category_id)
        .first()
    )
    if not session:
        raise HTTPException(status_code=404, detail="Session not found in this category")

    new_review = ReviewModel(**review.dict(), user_id= current_user.id, session_id=session_id)

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review



