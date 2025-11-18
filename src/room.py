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
        self.current_guest = None

    def mark_booked(self, guest):
        """
        Change the current room state to booked if room is available or not already booked
        """

        if self.status in [RoomStatus.AVAILABLE, RoomStatus.CLEANING]:
            self.status = RoomStatus.BOOKED
            self.current_guest = guest
            print(f"📝 Room {self.room_number} booked by {guest.name}")
        elif self.status == RoomStatus.BOOKED:
            print(f"⚠️ Room {self.room_number} is already booked by {self.current_guest.name}")
        elif self.status == RoomStatus.OCCUPIED:
            print(f"❌ Room {self.room_number} is being occupied by {self.current_guest.name}")

    def check_in(self):
        """
        Proceed with check-in after some conditions
        """

        if self.status == RoomStatus.BOOKED:
            self.status = RoomStatus.OCCUPIED
            print(f"✅ {self.current_guest.name} checked into Room {self.room_number}.")
        elif self.status == RoomStatus.AVAILABLE:
            print(f"❌ Cannot check in: Room {self.room_number} is not booked.")
        elif self.status == RoomStatus.OCCUPIED:
            print(f"⚠️ Room {self.room_number} is already occupied by {self.current_guest.name}.")
        elif self.status == RoomStatus.CLEANING:
            print(f"🧹 Cannot check in: Room {self.room_number} is still being cleaned.")

    def check_out(self):
        """
        Performs check-out if the room is occupied. After checkout, the room goes into cleaning state.
        """

        if self.status == RoomStatus.OCCUPIED:
            print(f"🔓 {self.current_guest.name} checked out from Room {self.room_number}.")
            self.current_guest = None
            self.status = RoomStatus.CLEANING
            print(f"🧹 Room {self.room_number} is now under cleaning.")
        elif self.status == RoomStatus.BOOKED:
            print(f"❌ Guest must check in before checking out.")
        elif self.status == RoomStatus.AVAILABLE:
            print(f"⚠️ Room {self.room_number} is already available.")
        elif self.status == RoomStatus.CLEANING:
            print(f"⚠️ Room {self.room_number} is already being cleaned.")

    def mark_cleaned(self, staff_member):
        """
        Marks the room as cleaned and available again.
        """

        from staff import Staff

        if not isinstance(staff_member, Staff):
            print("❌ Only staff members can perform this action.")

        if staff_member.role != "cleaner":
            print(f"{staff_member.name} ({staff_member.role}) is not authorized to perform cleaning operations.")

        if self.status == RoomStatus.CLEANING:
            self.status = RoomStatus.AVAILABLE
            print(f"✅ Room {self.room_number} has been cleaned and is now available.")
        else:
            print(f"❌ Only rooms currently being cleaned can be marked as cleaned.")

    def mark_cancelled(self):
        """
        Cancels an existing booking and makes the room available again.
        """

        if self.status == RoomStatus.BOOKED:
            print(f"🚫 Room {self.room_number} cancelled by {self.current_guest.name}")
            self.current_guest = None
            self.status = RoomStatus.AVAILABLE
        elif self.status == RoomStatus.AVAILABLE:
            print(f"❌ Room {self.room_number} has no active booking to cancel.")
        elif self.status == RoomStatus.OCCUPIED:
            print(f"❌ Cannot cancel booking: Room {self.room_number} is occupied.")
        elif self.status == RoomStatus.CLEANING:
            print(f"⚠️ Room {self.room_number} is being cleaned and has no active booking.")

    def show_details(self):
        guest_name = self.current_guest.name if self.current_guest else "None"
        print(f"Room {self.room_number} | Type: {self.room_type} | Status: {self.status.value.title()} | Current Guest: {guest_name}")

    def __str__(self):
        guest = f" - Guest: {self.current_guest.name}" if self.current_guest else ""
        return f"Room {self.room_number} ({self.room_type}) - {self.status.value.title()}{guest}"