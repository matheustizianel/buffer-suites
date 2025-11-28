from src.db.engine import engine
from src.db.base import Base

from src.models import GuestModel, RoomModel, ReservationModel

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()