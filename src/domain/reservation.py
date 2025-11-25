from datetime import datetime
from enum import Enum
from src.domain.room import RoomStatus

class ReservationStatus(Enum):
    ACTIVE = "active"
    CHECKED_IN = "checked_in"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Reservation:
    def __init__(self, guest, room):
        self.guest = guest
        self.room = room

        self.booking_time = None
        self.checkin_time = None
        self.checkout_time = None
        self.cancellation_time = None

        self.status = None

    def reserve(self):
        if self.room.status != RoomStatus.AVAILABLE:
            raise Exception(f"Room {self.room.room_number} is not available")
        
        self.booking_time = datetime.now()
        self.status = ReservationStatus.ACTIVE
        self.room.set_status(RoomStatus.BOOKED)

        print(f"📝 Reservation confirmed for {self.guest.name} in room {self.room.room_number} at {self.booking_time}")

    def check_in(self):
        if self.room.status != RoomStatus.BOOKED:
            raise Exception("You must make a reservation before checking-in.")
        
        self.checkin_time = datetime.now()
        self.status = ReservationStatus.CHECKED_IN
        self.room.set_status(RoomStatus.OCCUPIED)

        print(f"✅ {self.guest.name} checked in room {self.room.room_number} at {self.checkin_time}")

    def check_out(self):
        if self.room.status != RoomStatus.OCCUPIED:
            raise Exception(f"Room must be occupied in order to check-out.")
        
        self.checkout_time = datetime.now()
        self.status = ReservationStatus.COMPLETED
        self.room.set_status(RoomStatus.CLEANING)

        print(f"🔓 {self.guest.name} checked out from room {self.room.room_number} at {self.checkout_time}")

    def cancel(self):
        if self.room.status != RoomStatus.BOOKED:
            raise Exception("Cannot cancel a reservation that is not booked.")
        
        self.cancellation_time = datetime.now()
        self.status = ReservationStatus.CANCELLED
        self.room.set_status(RoomStatus.AVAILABLE)

        print(f"Reservation cancelled at {self.cancellation_time} by {self.guest.name}")

    def __str__(self):
        return f"{self.guest.name}, Room {self.room.room_number}, Status: {self.status.value}"

    def __repr__(self):
        return self.__str__()