from sqlalchemy import Column, Integer, String

from ..db.base import Base

class StaffModel(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    role = Column(String, nullable = False)
    email = Column(String, nullable = True)
    phone_number = Column(String, nullable = True)
    address = Column(String, nullable = True)

    def __repr__(self):
        return f"<Staff (id={self.id}, name={self.name}, role={self.role})>"