from datetime import datetime

class Guest:
    def __init__(self, name):
        self.name = name
        self.room = None
        self.booking_time = None
        self.checkin_time = None
        self.checkout_time = None

    def book_room(self, room):
        room.mark_booked(self.name)
        self.room = room
        self.booking_time = datetime.now()
        print(f"Room booked at {self.booking_time.strftime("%m/%d/%Y - %H:%M:%S")}")

    def check_in(self):
        room = self.room
        room.assign_guest(self.name)
        self.checkin_time = datetime.now()
        print(f"Checkin complete.")
        print(f"Checkin time: {self.checkin_time.strftime("%m/%d/%Y - %H:%M:%S")}")

    def check_out(self):
        room = self.room
        room.remove_guest()
        print("checkout complete")
        print(f"Checkout time: {self.checkin_time.strftime("%m/%d/%Y - %H:%M:%S")}")