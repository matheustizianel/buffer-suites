from enum import Enum

class RoomStatus(Enum):
    AVAILABLE = "available"
    BOOKED = "booked"
    OCCUPIED = "occupied"
    CLEANING = "cleaning"

class Room:
    """
    Represents a hotel room, including its state transitions.
    """

    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.status = RoomStatus.AVAILABLE

    def set_status(self, new_status):
        self.status = new_status

    def show_details(self):
        print(f"Room {self.room_number} | Type: {self.room_type} | Status: {self.status.value.title()}")