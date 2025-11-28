from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..db.base import Base

class GuestModel(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    email = Column(String, nullable = True)
    phone_number = Column(String, nullable = True)
    address = Column(String, nullable = True)

    reservations = relationship("ReservationModel", back_populates = "guest")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
        }

    def __str__(self):
        return f"{self.name} (ID {self.id})"

    def __repr__(self):
        return f"<Guest {self.id}: {self.name}>"
