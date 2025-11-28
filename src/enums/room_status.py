from enum import Enum

class RoomStatus(Enum):
    AVAILABLE = "available"
    BOOKED = "booked"
    OCCUPIED = "occupied"