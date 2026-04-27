from src.db.engine import engine
from src.db.base import Base

from src.models.guest_model import GuestModel
from src.models.room_model import RoomModel
from src.models.reservation_model import ReservationModel

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()