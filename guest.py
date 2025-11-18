from datetime import datetime
from person import Person

class Guest(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.room = None

        self.booking_time = None
        self.checkin_time = None
        self.checkout_time = None
        self.cancelling_time = None

    def book_room(self, room):
        room.mark_booked(self)
        if room.current_guest == self:
            self.room = room
            self.booking_time = datetime.now()
            print(f"{self.name} booked room {room.room_number} at {self.booking_time.strftime('%m/%d/%Y - %H:%M:%S')}")

    def cancel_booking(self, room):
        """
        Cancel the room booked for this guest
        """

        self.room = room
        self.room.mark_cancelled()
        self.cancelling_time = datetime.now()
        print(f"{self.name} cancelled room {room.room_number} at {self.cancelling_time.strftime('%m/%d/%Y - %H:%M:%S')}")
        self.room = None