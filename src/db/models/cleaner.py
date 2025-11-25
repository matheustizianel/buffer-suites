from sqlalchemy import Column, Integer, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship

from ...domain.staff import StaffShift
from ..base import Base

class CleanerModel(Base):
    __tablename__ = "cleaners"

    id = Column(Integer, primary_key = True, index = True)
    staff_id = Column(Integer, ForeignKey("staff.id"), nullable = False)
    shift = Column(Enum(StaffShift), nullable = False)
    is_on_shift = Column(Boolean, default = True)

    staff = relationship("StaffModel")

    def __repr__(self):
        return f"<Cleaner (id={self.id}, staff_id={self.staff_id}, shift={self.shift})>"
