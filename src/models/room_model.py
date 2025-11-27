from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from ..enums.room_status import RoomStatus
from ..db.base import Base

class RoomModel(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key = True, index = True)
    room_number = Column(Integer, nullable = False, unique = True)
    room_type = Column(String, nullable = False)
    status = Column(Enum(RoomStatus), nullable = False)

    reservations = relationship("ReservationModel", back_populates = "room")

    def __repr__(self):
        return f"<Room (id={self.id}, number={self.room_number}, status={self.status})>" 