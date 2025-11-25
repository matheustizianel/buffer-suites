from .engine import engine
from .base import Base

from .models import GuestModel, StaffModel, CleanerModel, RoomModel, ReservationModel

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()