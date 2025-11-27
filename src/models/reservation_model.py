from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship

from ..enums.reservation_status import ReservationStatus
from ..db.base import Base

class ReservationModel(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key = True, index = True)
    guest_id = Column(Integer, ForeignKey("guests.id"), nullable = False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable = False)

    booking_time = Column(DateTime, nullable = True)
    checkin_time = Column(DateTime, nullable = True)
    checkout_time = Column(DateTime, nullable = True)
    cancellation_time = Column(DateTime, nullable = True)
    
    status = Column(Enum(ReservationStatus), nullable = False)

    guest = relationship("GuestModel", back_populates = "reservations")
    room = relationship("RoomModel", back_populates = "reservations")

    def __repr__(self):
        return f"<Reservation (id={self.id}, guest={self.guest_id}, room={self.room_id}, status={self.status})>"