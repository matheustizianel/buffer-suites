from sqlalchemy import Column, Integer, String, ForeignKey
from src.db.base import Base


class ReviewModel(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    content = Column(String, nullable=False)