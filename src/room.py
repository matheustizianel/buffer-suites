from enum import Enum
from src.cleaner import Cleaner

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

    def mark_cleaned(self, staff_member):
        if not isinstance(staff_member, Cleaner):
            raise Exception(f"Staff member {staff_member.name} is not allowed to clean rooms.")

        if self.status != RoomStatus.CLEANING:
            raise Exception(f"Room {self.room_number} must be in cleaning state before being marked as cleaned.")

        self.set_status(RoomStatus.AVAILABLE)

        print(f"Room {self.room_number} is now AVAILABLE after after being cleaned by {staff_member.name}.")



    def show_details(self):
        print(f"Room {self.room_number} | Type: {self.room_type} | Status: {self.status.value.title()}")

    def __str__(self):
        return f"{self.room_number} | {self.room_type} | {self.status.value.title()}"

    def __repr__(self):
        return self.__str__()