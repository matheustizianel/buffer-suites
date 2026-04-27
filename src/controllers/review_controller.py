from src.db.session import SessionLocal
from src.models.review_model import ReviewModel

class ReviewController:

    @staticmethod
    def create_review(room_id, content):
        db = SessionLocal()
        review = ReviewModel(room_id=room_id, content=content)
        db.add(review)
        db.commit()
        db.refresh(review)
        db.close()
        return review

    @staticmethod
    def get_reviews_by_room(room_id):
        db = SessionLocal()
        reviews = db.query(ReviewModel).filter_by(room_id=room_id).all()
        db.close()
        return reviews